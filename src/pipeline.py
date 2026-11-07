"""Main Orchestration Pipeline for Enterprise AI Content Studio.

Executes the end-to-end workflow:
GitHub Release -> Script -> Voiceover -> Descript Underlord Editing -> Buffer LinkedIn Scheduling.
"""

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Dict, Optional

from .quota_manager import QuotaManager
from .github_analyzer import GitHubAnalyzer, ReleaseHighlight
from .script_generator import ScriptGenerator, VideoScript
from .voiceover_synthesizer import VoiceoverSynthesizer, VoiceoverResult
from .descript_orchestrator import DescriptOrchestrator, DescriptJobResult
from .buffer_publisher import BufferPublisher, PublishScheduleResult


@dataclass
class PipelineRunReport:
    release_highlight: ReleaseHighlight
    script: VideoScript
    voiceover: VoiceoverResult
    descript: DescriptJobResult
    buffer: PublishScheduleResult
    quota_snapshot: Dict[str, Any]
    dry_run: bool


class ContentPipeline:
    """Master pipeline orchestrating AI video creation from software releases."""

    def __init__(
        self,
        output_dir: Optional[Path] = None,
        quota_manager: Optional[QuotaManager] = None,
    ):
        self.output_dir = output_dir or Path("output")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.quota_mgr = quota_manager or QuotaManager()
        self.github_analyzer = GitHubAnalyzer()
        self.script_gen = ScriptGenerator()
        self.voice_synth = VoiceoverSynthesizer(output_dir=self.output_dir / "audio")
        self.descript_orch = DescriptOrchestrator()
        self.buffer_pub = BufferPublisher()

    def run(
        self,
        format_type: str = "linkedin-60s",
        force_dry_run: bool = False,
    ) -> PipelineRunReport:
        """Executes the pipeline with automatic quota guarding."""
        # 1. Inspect GitHub changes
        highlight = self.github_analyzer.get_latest_release_or_mock()

        # 2. Generate video script
        if format_type == "short-30s":
            script = self.script_gen.generate_short_30s(highlight)
        elif format_type == "demo-3m":
            script = self.script_gen.generate_demo_3m(highlight)
        else:
            script = self.script_gen.generate_linkedin_60s(highlight)

        est_minutes = script.target_duration_sec / 60.0
        est_chars = len(script.full_voiceover)

        # 3. Quota check & dry-run evaluation
        capacity = self.quota_mgr.check_capacity(est_minutes, est_chars)
        is_dry_run = force_dry_run or (not capacity["can_proceed"])

        # 4. Synthesize voiceover
        voice_res = self.voice_synth.synthesize(
            text=script.full_voiceover,
            filename_prefix=f"{highlight.tag}_{format_type}",
            dry_run=is_dry_run,
        )

        # 5. Descript orchestration & Underlord edits
        descript_res = self.descript_orch.execute_video_production(
            script=script,
            audio_path=voice_res.audio_path,
            dry_run=is_dry_run,
        )

        # 6. Buffer post formatting and scheduling
        buffer_res = self.buffer_pub.schedule_post(
            highlight=highlight,
            descript_result=descript_res,
            dry_run=is_dry_run,
        )

        # 7. Record usage in quota manager
        self.quota_mgr.record_usage(
            action=f"Generate {format_type} for {highlight.tag}",
            descript_minutes=est_minutes,
            elevenlabs_chars=est_chars,
            dry_run=is_dry_run,
        )

        # 8. Persist run manifest
        run_manifest = {
            "format": format_type,
            "release": highlight.tag,
            "dry_run": is_dry_run,
            "video_url": descript_res.publish_url,
            "social_copy": buffer_res.post_text,
            "transcript": descript_res.transcript_text,
            "scenes": [
                {
                    "scene": s.scene_number,
                    "duration": s.duration_sec,
                    "cue": s.visual_cue,
                    "voiceover": s.voiceover_text,
                    "underlord": s.underlord_prompt,
                }
                for s in script.scenes
            ],
        }
        manifest_file = self.output_dir / f"manifest_{highlight.tag}_{format_type}.json"
        manifest_file.write_text(json.dumps(run_manifest, indent=2))

        return PipelineRunReport(
            release_highlight=highlight,
            script=script,
            voiceover=voice_res,
            descript=descript_res,
            buffer=buffer_res,
            quota_snapshot=self.quota_mgr.get_status_report(),
            dry_run=is_dry_run,
        )
