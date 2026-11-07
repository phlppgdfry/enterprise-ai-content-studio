"""Quota Manager for Free-Tier AI Video Production.

Guards Descript transcription minutes and ElevenLabs voice characters
to ensure workflows do not exceed monthly free plan limits.
Supports dry-run simulation mode and rollover tracking.
"""

from dataclasses import dataclass, field
import datetime
import json
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class UsageRecord:
    timestamp: str
    action: str
    descript_minutes: float
    elevenlabs_chars: int
    dry_run: bool


class QuotaManager:
    """Tracks and enforces free-tier quotas across billing cycles."""

    DEFAULT_STATE_FILE = Path("quota_state.json")

    def __init__(
        self,
        state_file: Optional[Path] = None,
        max_descript_minutes: float = 60.0,
        max_elevenlabs_chars: int = 10000,
        auto_simulate: bool = True,
    ):
        self.state_file = state_file or self.DEFAULT_STATE_FILE
        self.max_descript_minutes = max_descript_minutes
        self.max_elevenlabs_chars = max_elevenlabs_chars
        self.auto_simulate = auto_simulate
        self.state: Dict[str, Any] = self._load_or_init_state()

    def _get_current_month_key(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m")

    def _get_next_reset_date(self) -> str:
        now = datetime.datetime.now()
        # Next month 1st
        year = now.year + (1 if now.month == 12 else 0)
        month = 1 if now.month == 12 else now.month + 1
        reset = datetime.datetime(year, month, 1, 0, 0, 0)
        return reset.strftime("%Y-%m-%d %H:%M:%S")

    def _load_or_init_state(self) -> Dict[str, Any]:
        current_month = self._get_current_month_key()
        if self.state_file.exists():
            try:
                data = json.loads(self.state_file.read_text())
                if data.get("current_month") == current_month:
                    return data
                # Rollover detected: archive previous month and reset current counters
                return self._rollover_state(data, current_month)
            except Exception:
                pass

        return {
            "current_month": current_month,
            "next_reset_date": self._get_next_reset_date(),
            "descript_minutes_used": 0.0,
            "descript_minutes_limit": self.max_descript_minutes,
            "elevenlabs_chars_used": 0,
            "elevenlabs_chars_limit": self.max_elevenlabs_chars,
            "history": [],
        }

    def _rollover_state(self, old_data: Dict[str, Any], current_month: str) -> Dict[str, Any]:
        """Automatically resets monthly usage counters when a new month begins."""
        archived = old_data.get("history", [])
        return {
            "current_month": current_month,
            "next_reset_date": self._get_next_reset_date(),
            "descript_minutes_used": 0.0,
            "descript_minutes_limit": self.max_descript_minutes,
            "elevenlabs_chars_used": 0,
            "elevenlabs_chars_limit": self.max_elevenlabs_chars,
            "previous_cycle_summary": {
                "month": old_data.get("current_month"),
                "descript_minutes": old_data.get("descript_minutes_used", 0.0),
                "elevenlabs_chars": old_data.get("elevenlabs_chars_used", 0),
            },
            "history": archived[-50:],  # keep last 50 entries
        }

    def save(self) -> None:
        self.state_file.write_text(json.dumps(self.state, indent=2))

    def check_capacity(self, estimated_minutes: float, estimated_chars: int) -> Dict[str, Any]:
        """Checks if there is remaining capacity under the free tier budget."""
        used_min = self.state["descript_minutes_used"]
        used_chars = self.state["elevenlabs_chars_used"]

        has_descript = (used_min + estimated_minutes) <= self.max_descript_minutes
        has_elevenlabs = (used_chars + estimated_chars) <= self.max_elevenlabs_chars

        remaining_min = max(0.0, self.max_descript_minutes - used_min)
        remaining_chars = max(0, self.max_elevenlabs_chars - used_chars)

        can_proceed = has_descript and has_elevenlabs

        return {
            "can_proceed": can_proceed,
            "should_simulate": not can_proceed and self.auto_simulate,
            "descript": {
                "requested": estimated_minutes,
                "used": used_min,
                "limit": self.max_descript_minutes,
                "remaining": remaining_min,
                "fits": has_descript,
            },
            "elevenlabs": {
                "requested": estimated_chars,
                "used": used_chars,
                "limit": self.max_elevenlabs_chars,
                "remaining": remaining_chars,
                "fits": has_elevenlabs,
            },
            "next_reset_date": self.state["next_reset_date"],
        }

    def record_usage(
        self,
        action: str,
        descript_minutes: float,
        elevenlabs_chars: int,
        dry_run: bool = False,
    ) -> None:
        """Records an action in the history and updates usage counters if not dry-run."""
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action,
            "descript_minutes": descript_minutes,
            "elevenlabs_chars": elevenlabs_chars,
            "dry_run": dry_run,
        }
        self.state.setdefault("history", []).append(record)

        if not dry_run:
            self.state["descript_minutes_used"] += descript_minutes
            self.state["elevenlabs_chars_used"] += elevenlabs_chars

        self.save()

    def get_status_report(self) -> Dict[str, Any]:
        used_min = self.state["descript_minutes_used"]
        used_chars = self.state["elevenlabs_chars_used"]
        pct_descript = (used_min / self.max_descript_minutes) * 100 if self.max_descript_minutes > 0 else 0
        pct_elevenlabs = (used_chars / self.max_elevenlabs_chars) * 100 if self.max_elevenlabs_chars > 0 else 0

        return {
            "month": self.state["current_month"],
            "next_reset": self.state["next_reset_date"],
            "descript": {
                "used": round(used_min, 2),
                "limit": self.max_descript_minutes,
                "remaining": round(max(0.0, self.max_descript_minutes - used_min), 2),
                "percentage": round(pct_descript, 1),
            },
            "elevenlabs": {
                "used": used_chars,
                "limit": self.max_elevenlabs_chars,
                "remaining": max(0, self.max_elevenlabs_chars - used_chars),
                "percentage": round(pct_elevenlabs, 1),
            },
            "total_actions": len(self.state.get("history", [])),
        }
