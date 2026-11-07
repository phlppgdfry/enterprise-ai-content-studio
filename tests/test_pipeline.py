"""Integration tests for ContentPipeline in dry-run/safe mode."""

from pathlib import Path
import pytest
from src.pipeline import ContentPipeline
from src.quota_manager import QuotaManager


def test_pipeline_dry_run_execution(tmp_path: Path):
    quota_file = tmp_path / "test_quota.json"
    qm = QuotaManager(state_file=quota_file)
    pipeline = ContentPipeline(output_dir=tmp_path / "output", quota_manager=qm)

    report = pipeline.run(format_type="linkedin-60s", force_dry_run=True)

    assert report.dry_run is True
    assert report.script.target_duration_sec == 60.0
    assert len(report.script.scenes) == 4
    assert report.voiceover.is_simulated is True
    assert report.descript.is_simulated is True
    assert "https://share.descript.com/view/" in report.descript.publish_url
    assert "Nieuwe release:" in report.buffer.post_text


def test_pipeline_vertical_short_execution(tmp_path: Path):
    quota_file = tmp_path / "test_quota.json"
    qm = QuotaManager(state_file=quota_file)
    pipeline = ContentPipeline(output_dir=tmp_path / "output", quota_manager=qm)

    report = pipeline.run(format_type="short-30s", force_dry_run=True)

    assert report.dry_run is True
    assert report.script.target_duration_sec == 30.0
    assert report.script.aspect_ratio == "9:16"
