"""Interactive CLI for Enterprise AI Content Studio.

Commands:
  run          Execute automated release-to-video pipeline
  quota        View monthly Descript & ElevenLabs usage and reset dates
  plan         Print the 30-day curriculum and Descript Expert badge roadmap
  simulate     Run complete pipeline in simulation mode (preserves credits)
"""

import sys
from pathlib import Path

# Ensure root package is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Safe environment loading without hard dependency on python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        import os
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())



from src.pipeline import ContentPipeline
from src.quota_manager import QuotaManager


def print_banner():
    print("""
========================================================================
🎬 ENTERPRISE AI CONTENT AUTOMATION STUDIO
   Descript Underlord + ElevenLabs + GitHub + Buffer Pipeline
========================================================================
""")


def cmd_run(format_type: str = "linkedin-60s", dry_run: bool = False):
    print_banner()
    print(f"🚀 Starting pipeline for format: [bold cyan]{format_type}[/]...")
    if dry_run:
        print("🛡️  Safe Mode Enabled: Dry-run execution (No real credits consumed)")

    pipeline = ContentPipeline()
    report = pipeline.run(format_type=format_type, force_dry_run=dry_run)

    print("\n------------------------------------------------------------------------")
    print("✅ PIPELINE EXECUTION COMPLETED")
    print("------------------------------------------------------------------------")
    print(f"📦 Release Analyzed : {report.release_highlight.title} ({report.release_highlight.tag})")
    print(f"⏱️  Duration Target   : {report.script.target_duration_sec}s ({len(report.script.scenes)} scenes)")
    print(f"🎙️  Audio Voiceover   : {report.voiceover.audio_path} ({'Simulated' if report.voiceover.is_simulated else 'ElevenLabs API'})")
    print(f"🎬 Descript Video    : {report.descript.publish_url} ({'Simulated' if report.descript.is_simulated else 'Live Descript'})")
    print(f"📢 Buffer Status     : {report.buffer.status} -> {report.buffer.scheduled_time}")

    print("\n------------------------------------------------------------------------")
    print("📝 GENERATED LINKEDIN COPY:")
    print("------------------------------------------------------------------------")
    print(report.buffer.post_text)

    print("\n------------------------------------------------------------------------")
    print("📊 MONTHLY FREE-TIER QUOTA STATUS:")
    print("------------------------------------------------------------------------")
    q = report.quota_snapshot
    print(f"Month Cycle       : {q['month']} (Next rollover reset: {q['next_reset']})")
    print(f"Descript Minutes  : {q['descript']['used']} / {q['descript']['limit']} min ({q['descript']['percentage']}%) | Remaining: {q['descript']['remaining']} min")
    print(f"ElevenLabs Chars  : {q['elevenlabs']['used']} / {q['elevenlabs']['limit']} chars ({q['elevenlabs']['percentage']}%) | Remaining: {q['elevenlabs']['remaining']} chars")
    print("------------------------------------------------------------------------\n")


def cmd_quota():
    print_banner()
    qm = QuotaManager()
    q = qm.get_status_report()
    print("📊 CURRENT FREE-TIER USAGE & CAPACITY GUARD")
    print("------------------------------------------------------------------------")
    print(f"Billing Cycle      : {q['month']}")
    print(f"Next Monthly Reset : {q['next_reset']}")
    print("------------------------------------------------------------------------")
    print(f"🎬 Descript Transcription & AI Edit:")
    print(f"   Used      : {q['descript']['used']} minutes")
    print(f"   Limit     : {q['descript']['limit']} minutes")
    print(f"   Remaining : {q['descript']['remaining']} minutes ({100 - q['descript']['percentage']}%)")
    print(f"\n🎙️  ElevenLabs Voice Synthesis:")
    print(f"   Used      : {q['elevenlabs']['used']} characters")
    print(f"   Limit     : {q['elevenlabs']['limit']} characters")
    print(f"   Remaining : {q['elevenlabs']['remaining']} characters ({100 - q['elevenlabs']['percentage']}%)")
    print(f"\n📁 Total Pipeline Operations Run: {q['total_actions']}")
    print("------------------------------------------------------------------------\n")


def cmd_plan():
    print_banner()
    print("""
🏆 30-DAGEN ROUTE NAAR DESCRIPT EXPERT + LINKEDIN CERTIFICERING
------------------------------------------------------------------------
Doelstelling: 3 officiële niveaus (🥉 Proficient -> 🥈 Advanced -> 🥇 Expert)
verdiend via feature-gebruik, gecombineerd met een live GitHub portfolio.

WEEK 1: FUNDAMENTEN & BASISBEWERKING
  • Dag 1-2 : Screen recording & transcriptie
  • Dag 3-4 : Knippen via tekst, filler words wissen & Studio Sound
  • Dag 5-7 : Scènes indelen, ondertitels en eerste introductievideo (Project 1)

WEEK 2: UNDERLORD AI, AI SPEECH & LAYOUTS
  • Dag 8-10 : Underlord AI co-editor prompts & automatische B-roll
  • Dag 11-12: AI Speech voice cloning & visuele overlays
  • Dag 13-14: Uitgebreide 2-3 minuten productdemo (Project 2)

WEEK 3: MEERTALIGHEID & REPURPOSING
  • Dag 15-18: Nederlandse mastervideo vertalen naar EN en FR (Project 3)
  • Dag 19-21: 1 video opdelen in 60s LinkedIn, 30s Short, 30s Reel (Project 4)

WEEK 4: VOLLEDIGE AUTOMATISERING & LINKEDIN SHOWCASE
  • Dag 22-25: GitHub release analyzer & ElevenLabs pipeline koppelen (Project 5)
  • Dag 26-28: Buffer scheduling & LinkedIn showcase posts
  • Dag 29-30: Certificering badges claimen in Settings -> Connections

Bekijk TRACKER.md voor de interactieve voortgangsmatrix!
------------------------------------------------------------------------
""")


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help", "help"):
        print_banner()
        print("Usage: python3 src/cli.py <command> [options]\n")
        print("Commands:")
        print("  run [format]   Run pipeline (formats: linkedin-60s, short-30s, demo-3m)")
        print("  simulate       Run safe simulation (0 real credits consumed)")
        print("  quota          Check free-tier credit balance & next monthly reset")
        print("  plan           Display 30-day roadmap towards Descript Expert")
        sys.exit(0)

    cmd = args[0]
    if cmd == "run":
        fmt = args[1] if len(args) > 1 and not args[1].startswith("--") else "linkedin-60s"
        dry = "--dry-run" in args or "-d" in args
        cmd_run(format_type=fmt, dry_run=dry)
    elif cmd == "simulate":
        fmt = args[1] if len(args) > 1 else "linkedin-60s"
        cmd_run(format_type=fmt, dry_run=True)
    elif cmd == "quota":
        cmd_quota()
    elif cmd == "plan":
        cmd_plan()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
