"""Unit tests for QuotaManager."""

import json
from pathlib import Path
import pytest
from src.quota_manager import QuotaManager


def test_quota_manager_initialization(tmp_path: Path):
    state_file = tmp_path / "test_quota.json"
    qm = QuotaManager(state_file=state_file, max_descript_minutes=30.0, max_elevenlabs_chars=5000)

    report = qm.get_status_report()
    assert report["descript"]["limit"] == 30.0
    assert report["descript"]["used"] == 0.0
    assert report["descript"]["remaining"] == 30.0
    assert report["elevenlabs"]["limit"] == 5000
    assert report["elevenlabs"]["used"] == 0


def test_quota_manager_record_usage(tmp_path: Path):
    state_file = tmp_path / "test_quota.json"
    qm = QuotaManager(state_file=state_file, max_descript_minutes=10.0, max_elevenlabs_chars=1000)

    qm.record_usage("Test Run 1", descript_minutes=2.5, elevenlabs_chars=250, dry_run=False)
    report = qm.get_status_report()
    assert report["descript"]["used"] == 2.5
    assert report["descript"]["remaining"] == 7.5
    assert report["elevenlabs"]["used"] == 250
    assert report["elevenlabs"]["remaining"] == 750

    # Dry-run should not increment counters
    qm.record_usage("Simulated Run", descript_minutes=5.0, elevenlabs_chars=500, dry_run=True)
    report_dry = qm.get_status_report()
    assert report_dry["descript"]["used"] == 2.5
    assert report_dry["elevenlabs"]["used"] == 250
    assert report_dry["total_actions"] == 2


def test_quota_capacity_check(tmp_path: Path):
    state_file = tmp_path / "test_quota.json"
    qm = QuotaManager(state_file=state_file, max_descript_minutes=5.0, max_elevenlabs_chars=500)

    # Fits
    res = qm.check_capacity(estimated_minutes=2.0, estimated_chars=200)
    assert res["can_proceed"] is True

    # Exceeds
    res_exceed = qm.check_capacity(estimated_minutes=6.0, estimated_chars=200)
    assert res_exceed["can_proceed"] is False
    assert res_exceed["should_simulate"] is True
