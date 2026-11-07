"""AI Video Script Generator.

Generates structured video scripts with visual cues, voiceover lines,
and Underlord AI prompts tailored for LinkedIn, YouTube Shorts, and Product Demos.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List
from .github_analyzer import ReleaseHighlight


@dataclass
class SceneCue:
    scene_number: int
    duration_sec: float
    visual_cue: str
    voiceover_text: str
    underlord_prompt: str


@dataclass
class VideoScript:
    project_title: str
    format_type: str  # "linkedin-60s", "short-30s", "demo-3m"
    target_duration_sec: float
    aspect_ratio: str  # "16:9", "9:16", "1:1"
    scenes: List[SceneCue] = field(default_factory=list)

    @property
    def total_words(self) -> int:
        return sum(len(s.voiceover_text.split()) for s in self.scenes)

    @property
    def full_voiceover(self) -> str:
        return " ".join(s.voiceover_text for s in self.scenes)


class ScriptGenerator:
    """Produces multi-format video scripts based on release highlights."""

    def generate_linkedin_60s(self, highlight: ReleaseHighlight) -> VideoScript:
        """Generates an executive 60-second video script for LinkedIn."""
        scenes = [
            SceneCue(
                scene_number=1,
                duration_sec=8.0,
                visual_cue="Hook: High-contrast title card with project logo and dynamic animated headline",
                voiceover_text=f"Wat als elke software-update automatisch binnen twee minuten verandert in een professionele videodemonstratie? Maak kennis met {highlight.title}.",
                underlord_prompt="Add bold dynamic animated captions with brand highlight color. Zoom in 10% on key title.",
            ),
            SceneCue(
                scene_number=2,
                duration_sec=18.0,
                visual_cue="Problem & Context: Screen capture of raw code commits and traditional tedious video editing software",
                voiceover_text="Developers bouwen continu waardevolle features, maar handmatige contentcreatie en video-montage kost uren tijd. Deze release lost dat op.",
                underlord_prompt="Split screen: code commit diff on the left, video timeline on the right. Remove background noise with Studio Sound.",
            ),
            SceneCue(
                scene_number=3,
                duration_sec=22.0,
                visual_cue="Solution: Live walkthrough of automated workflow (GitHub -> ElevenLabs -> Descript -> Buffer)",
                voiceover_text=f"Onze nieuwe pipeline analyseert de release direct. Belangrijkste innovaties: {', '.join(highlight.features[:3])}. Alles gemonteerd en getiteld door Descript Underlord.",
                underlord_prompt="Add smooth slide transition. Apply auto-captions and highlight spoken words. Insert clean lower-third badge.",
            ),
            SceneCue(
                scene_number=4,
                duration_sec=12.0,
                visual_cue="Call to Action: Repository link, live dashboard preview, and LinkedIn connect invitation",
                voiceover_text="Bekijk de complete architectuur en open-source workflow op GitHub. Link in de eerste reactie!",
                underlord_prompt="Add subtle background music fade-out and display GitHub repo URL with animated arrow.",
            ),
        ]
        return VideoScript(
            project_title=f"{highlight.tag} - LinkedIn Executive Demo",
            format_type="linkedin-60s",
            target_duration_sec=60.0,
            aspect_ratio="16:9",
            scenes=scenes,
        )

    def generate_short_30s(self, highlight: ReleaseHighlight) -> VideoScript:
        """Generates a fast-paced 30-second vertical video for YouTube Shorts / Reels."""
        scenes = [
            SceneCue(
                scene_number=1,
                duration_sec=5.0,
                visual_cue="9:16 vertical hook with oversized emoji caption and swift punchy movement",
                voiceover_text="Stop met handmatig video's editen voor je code projecten!",
                underlord_prompt="Vertical 9:16 layout. Center subject with automatic face tracking. Word-by-word viral captions.",
            ),
            SceneCue(
                scene_number=2,
                duration_sec=15.0,
                visual_cue="Rapid-fire demonstration of the terminal running 'studio run' and Descript generating video in real time",
                voiceover_text=f"Met één commando pakt onze AI de nieuwste release van {highlight.tag}, maakt voiceover, knipt stiltes weg en plant de LinkedIn post.",
                underlord_prompt="Speed up non-speaking clips 1.5x. Remove all filler words and pauses > 0.4s.",
            ),
            SceneCue(
                scene_number=3,
                duration_sec=10.0,
                visual_cue="Final result preview and prompt to check GitHub",
                voiceover_text="Bouw het zelf na. Check de repository in de comments!",
                underlord_prompt="Add high-energy outro sound and animated follow button.",
            ),
        ]
        return VideoScript(
            project_title=f"{highlight.tag} - 30s Vertical Viral Short",
            format_type="short-30s",
            target_duration_sec=30.0,
            aspect_ratio="9:16",
            scenes=scenes,
        )

    def generate_demo_3m(self, highlight: ReleaseHighlight) -> VideoScript:
        """Generates an in-depth 3-minute technical product demonstration."""
        scenes = [
            SceneCue(
                scene_number=1,
                duration_sec=20.0,
                visual_cue="Executive summary & presenter webcam overlay over architecture slide",
                voiceover_text=f"Welkom bij de technische walkthrough van {highlight.title}. In deze video laten we zien hoe enterprise content automation in de praktijk werkt.",
                underlord_prompt="Apply Picture-in-Picture layout with rounded webcam in top right. Enable Studio Sound at 80%.",
            ),
            SceneCue(
                scene_number=2,
                duration_sec=50.0,
                visual_cue="Architecture breakdown: GitHub webhook triggering CLI, extracting changelog, and formatting LLM prompts",
                voiceover_text="We beginnen bij de broncode. Zodra een git tag wordt gepusht, parseert onze analyzer alle commits en categoriseert ze in features, fixes en architectuur-updates.",
                underlord_prompt="Highlight code snippet with glowing outline. Pan across the workflow diagram smoothly.",
            ),
            SceneCue(
                scene_number=3,
                duration_sec=60.0,
                visual_cue="Descript Underlord AI & Voiceover: showing text-based editing, filler word removal, and multilingual dubbing",
                voiceover_text="Vervolgens genereren we de audio met ElevenLabs en laden dit in Descript. Descript verwijdert stopwoorden, balanceert de audio met Studio Sound en genereert meertalige ondertitels.",
                underlord_prompt="Show transcript view. Demonstrate one-click filler word removal and scene division.",
            ),
            SceneCue(
                scene_number=4,
                duration_sec=35.0,
                visual_cue="Buffer automation & quota governance dashboard",
                voiceover_text="Tot slot bewaakt de Quota Guard onze gratis API-minuten en plant Buffer de LinkedIn en video releases op het optimale tijdstip.",
                underlord_prompt="Display quota dashboard with green capacity indicators. Transition to final slide.",
            ),
            SceneCue(
                scene_number=5,
                duration_sec=15.0,
                visual_cue="Closing slide with contact and portfolio links",
                voiceover_text="Bedankt voor het kijken. Vergeet niet de repo te starren op GitHub en connect op LinkedIn!",
                underlord_prompt="Fade to black with gentle outro chime.",
            ),
        ]
        return VideoScript(
            project_title=f"{highlight.tag} - 3-Minute Technical Walkthrough",
            format_type="demo-3m",
            target_duration_sec=180.0,
            aspect_ratio="16:9",
            scenes=scenes,
        )
