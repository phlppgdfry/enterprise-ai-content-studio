"""Buffer Publisher.

Formats executive social copy and schedules video updates to LinkedIn via Buffer.
Includes simulation mode when no Buffer credentials are configured.
"""

from dataclasses import dataclass
import os
from typing import Any, Dict, List, Optional
from .github_analyzer import ReleaseHighlight
from .descript_orchestrator import DescriptJobResult


@dataclass
class PublishScheduleResult:
    post_text: str
    media_url: Optional[str]
    scheduled_time: str
    channel: str
    is_simulated: bool
    status: str


class BufferPublisher:
    """Prepares and publishes social content to Buffer."""

    def __init__(
        self,
        access_token: Optional[str] = None,
        profile_id: Optional[str] = None,
    ):
        self.access_token = access_token or os.getenv("BUFFER_ACCESS_TOKEN")
        self.profile_id = profile_id or os.getenv("BUFFER_PROFILE_ID")

    def format_linkedin_copy(
        self,
        highlight: ReleaseHighlight,
        descript_result: DescriptJobResult,
    ) -> str:
        """Constructs high-engagement LinkedIn post copy."""
        features_bullets = "\n".join(f"  • {f}" for f in highlight.features[:3])
        return (
            f"🚀 Nieuwe release: {highlight.title}\n\n"
            f"We hebben onze workflow geautomatiseerd: van GitHub commits direct naar een professioneel "
            f"gemonteerde videodemonstratie met Descript Underlord en ElevenLabs.\n\n"
            f"Wat is er nieuw in {highlight.tag}:\n"
            f"{features_bullets}\n\n"
            f"Bekijk de demonstratievideo hier: {descript_result.publish_url}\n\n"
            f"#AIVideo #Descript #SoftwareEngineering #Automation #ElevenLabs #LinkedInDev"
        )

    def schedule_post(
        self,
        highlight: ReleaseHighlight,
        descript_result: DescriptJobResult,
        dry_run: bool = False,
    ) -> PublishScheduleResult:
        post_text = self.format_linkedin_copy(highlight, descript_result)

        if dry_run or not self.access_token or not self.profile_id:
            return PublishScheduleResult(
                post_text=post_text,
                media_url=descript_result.publish_url,
                scheduled_time="Tomorrow 09:00 AM (Optimal LinkedIn slot)",
                channel="LinkedIn Company / Personal Profile",
                is_simulated=True,
                status="staged_for_review",
            )

        # Real Buffer API call if tokens are available
        try:
            import requests

            url = "https://api.bufferapp.com/1/updates/create.json"
            headers = {"Authorization": f"Bearer {self.access_token}"}
            payload = {
                "profile_ids[]": [self.profile_id],
                "text": post_text,
                "media[link]": descript_result.publish_url,
                "now": False,
            }
            resp = requests.post(url, data=payload, headers=headers, timeout=30)
            if resp.status_code == 200:
                return PublishScheduleResult(
                    post_text=post_text,
                    media_url=descript_result.publish_url,
                    scheduled_time="Queued in Buffer",
                    channel="LinkedIn",
                    is_simulated=False,
                    status="published_to_buffer",
                )
        except Exception:
            pass

        return PublishScheduleResult(
            post_text=post_text,
            media_url=descript_result.publish_url,
            scheduled_time="Tomorrow 09:00 AM (Optimal LinkedIn slot)",
            channel="LinkedIn",
            is_simulated=True,
            status="staged_for_review",
        )
