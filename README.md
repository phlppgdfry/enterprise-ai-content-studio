# 🎬 Enterprise AI Content Automation Studio

> **Transforming Software Releases into Professional Video Demos & Social Highlights using Descript Underlord, ElevenLabs, GitHub, and Buffer.**  
> Includes a 30-day curriculum to achieve **Descript Expert Certification on LinkedIn**, 5 turnkey portfolio projects, reusable Underlord skills, and an automated Free-Tier Quota Guard.

[![Descript Certified](https://img.shields.io/badge/Descript-Expert%20Track-blueviolet?style=for-the-badge&logo=video)](https://descript.com)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![MCP Enabled](https://img.shields.io/badge/MCP-Ready-000?style=for-the-badge&logo=anthropic)](https://github.com/descriptinc/descript-mcp)
[![LinkedIn Showcase](https://img.shields.io/badge/LinkedIn-Showcase%20Ready-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg?style=for-the-badge)](LICENSE)

---

## 📌 Executive Summary

Modern software development moves fast, but manual product marketing and video editing remain massive bottlenecks. Producing a 60-second release video typically requires hours of manual recording, silence trimming, filler-word cutting, voiceover recording, captioning, and social media scheduling.

**Enterprise AI Content Automation Studio** solves this by establishing a fully autonomous pipeline:
1. **GitHub Release Analysis**: Parses git commits and releases into categorized highlights.
2. **AI Video Script Synthesis**: Automatically formats multi-scene scripts with timing and visual cues.
3. **ElevenLabs Voiceover Generation**: Generates lifelike multilingual voice tracks.
4. **Descript Underlord AI Editing**: Automatically cleans filler words, applies Studio Sound, adds dynamic captions, inserts B-roll, and renders multiple aspect ratios.
5. **Buffer Social Scheduling**: Formats executive LinkedIn copy and stages video posts.
6. **Free-Tier Quota Guard**: Protects free plan limits with automatic rollover tracking and simulation fallback.

```text
GitHub Release ──► Changelog Parser ──► Script Generator ──► ElevenLabs Audio
                                                                  │
                                                                  ▼
Buffer LinkedIn ◄── Quality Approval ◄── Underlord AI Editing ◄── Descript Studio
```

---

## 🏆 Descript LinkedIn Certificeringen (3 Niveaus)

Sinds februari 2026 ondersteunt Descript officiële vaardigheidscertificeringen die direct verschijnen onder **Licenties & Certificeringen** op je LinkedIn-profiel:

| Niveau | Badge | Focusgebied | Doelstelling in dit project |
|---|---|---|---|
| **Niveau 1** | 🥉 **Proficient** | Basisvaardigheden | Screen recording, tekst-gebaseerd knippen, Studio Sound & captions |
| **Niveau 2** | 🥈 **Advanced** | Geavanceerde AI | Underlord AI co-editing, B-roll, AI Speech & multi-track layouts |
| **Niveau 3** | 🥇 **Expert** | Enterprise Beheersing | Meertalige dubbing, multi-format repurposing, CLI/MCP automatisering |

*Koppel je account in Descript via **Settings → Connections → LinkedIn**.*

---

## 🚀 De 5 Portfolio Projecten

Dit repository bevat uitgewerkte sjablonen, scripts en checklists voor 5 concrete projecten:

| # | Project | Doelstelling | Live Descript Output |
|---|---|---|---|
| **01** | [**Professional AI Video Editing**](projects/01-professional-editing/) | 60-90s Introductievideo van een softwareproject | [Share Link (1080p Video)](https://share.descript.com/view/ouPR3bkHdYF) • [Descript Project](https://web.descript.com/1118cbc9-2908-4bdb-acdb-646ec6f3140d) |
| **02** | [**AI Product Demo**](projects/02-ai-product-demo/) | 2-3 min Geavanceerde technische walkthrough | [Share Link (Product Demo)](https://share.descript.com/view/n558bow7wq4) • [Descript Project](https://web.descript.com/c5dc9c48-18c8-4cee-a9ee-5088522ff517) |
| **03** | [**Multilingual AI Content**](projects/03-multilingual-content/) | 1 Nederlandse video naar Engels en Frans | [Share Link (Multilingual FR)](https://share.descript.com/view/YoU6f892hEf) • [Descript Project](https://web.descript.com/70db0422-c8b0-4b2c-9204-fd51a01b52b6) |
| **04** | [**AI Content Repurposing**](projects/04-content-repurposing/) | 1 mastervideo naar 5 social formats | [Share Link (Viral Short)](https://share.descript.com/view/w0jmYmu2rhR) • [Descript Project](https://web.descript.com/d4f60ae9-aee8-4f2d-a561-3d8ee6c00da0) |
| **05** | [**Autonomous Production Studio**](projects/05-automated-pipeline/) | End-to-end geautomatiseerde release-to-video pipeline | [Share Link (Underlord CI/CD)](https://share.descript.com/view/9naJmnbTxl0) • [Descript Project](https://web.descript.com/d664473b-63eb-44ca-94fe-77da1efb6fa6) |
| **06** | [**Enterprise Masterclass Video (Flagship)**](projects/05-automated-pipeline/) | 1080p Full HD Video met ElevenLabs & Underlord AI | [Share Link (1080p Masterclass)](https://share.descript.com/view/YdMh3h95pT0) • [Descript Project](https://web.descript.com/5b6aa62b-e08e-444e-a6c8-a44646e6a7f7) |

---

## 🧠 Herbruikbare Underlord Skills

Descript introduceerde **Underlord Skills** — herbruikbare prompt-ketens voor consistente video-montage. Dit repository bundelt drie kant-en-klare Underlord workflows:

- 🎬 [**Product Demo Editor**](underlord-skills/product-demo-editor.md) — Gestandaardiseerde software walkthroughs met zooms op actieve UI-elementen.
- 📱 [**Professional LinkedIn Clips Extractor**](underlord-skills/linkedin-clips-extractor.md) — Highlight extractie met virale woord-voor-woord ondertiteling en mobile aspect ratio framing.
- 🌍 [**Multilingual Content Workflow**](underlord-skills/multilingual-workflow.md) — Geautomatiseerde transcript vertaling en spraaksynchronisatie.

---

## 🛡️ Free-Tier Quota Guard & Simulatiemodus

> *"Wat als ik een gratis Descript / ElevenLabs account heb?"*

Descript biedt op het gratis plan **60 minuten transcriptie per maand**. ElevenLabs biedt **10.000 karakters per maand**. 

Onze ingebouwde Quota Guard (`src/quota_manager.py`) zorgt dat je:
1. **Nooit per ongeluk over je limiet gaat**: Voorafgaand aan elke render berekent de pipeline het verwachte verbruik.
2. **Volledig veilig kunt testen via Simulatie**: Met `python3 src/cli.py simulate` test je de hele workflow inclusief git parsing, scriptgeneratie, mock-audio en Buffer-payloads **zonder 1 credit te verbruiken**.
3. **Automatische Maandelijkse Reset**: Berekent exact wanneer je nieuwe tegoed ingaat (elke 1e van de kalendermaand) en houdt het verbruik bij in `quota_state.json`.

---

## 💻 Installatie & Gebruik

### 1. Vereisten
- Python 3.10+
- Node.js & npm (voor de officiële `@descript/platform-cli`)

### 2. Setup
```bash
# Clone het repository
git clone https://github.com/phlppgdfry/enterprise-ai-content-studio.git
cd enterprise-ai-content-studio

# Installeer Python afhankelijkheden
pip install -r requirements.txt

# Kopieer configuratiebestand
cp .env.example .env
```

### 3. CLI Commando's
```bash
# Bekijk je actuele gratis tegoed en volgende resetdatum
python3 src/cli.py quota

# Voer een veilige simulatie uit (0 credits verbruikt)
python3 src/cli.py simulate

# Voer een echte geautomatiseerde run uit voor LinkedIn (60s video)
python3 src/cli.py run linkedin-60s

# Voer een run uit voor een verticale YouTube Short (30s video)
python3 src/cli.py run short-30s

# Bekijk de 30-dagen routekaart naar Descript Expert
python3 src/cli.py plan
```

### 4. Tests Draaien
```bash
pytest tests/ -v
```

---

## 🔗 Descript MCP Server Integratie

Dit project is compatibel met de officiële Descript remote MCP server:
```text
https://api.descript.com/v2/mcp
```

De server en de 5 officiële agent skills (`create-video`, `edit-project`, `publish-project`, `export-transcript`, `export-timeline`) zijn geconfigureerd voor **Claude Code**, **OpenAI Codex** en **Antigravity**.

---

## 📂 Repository Structuur

```text
enterprise-ai-content-studio/
├── .github/workflows/content-pipeline.yml # GitHub Actions CI release workflow
├── projects/                             # De 5 portfolio projecten
│   ├── 01-professional-editing/          # Project 1: Basis introductievideo
│   ├── 02-ai-product-demo/               # Project 2: AI Product demo (Underlord)
│   ├── 03-multilingual-content/          # Project 3: Meertalig (NL, EN, FR)
│   ├── 04-content-repurposing/           # Project 4: Repurposing (5 formats)
│   └── 05-automated-pipeline/            # Project 5: Autonomous End-to-End
├── underlord-skills/                     # Herbruikbare Descript Underlord skills
│   ├── product-demo-editor.md
│   ├── linkedin-clips-extractor.md
│   └── multilingual-workflow.md
├── src/                                  # Pipeline orchestratie code
│   ├── cli.py                            # Interactive CLI
│   ├── quota_manager.py                  # Free-tier quota guard & rollover tracker
│   ├── github_analyzer.py                # Release & changelog parser
│   ├── script_generator.py               # AI script generator
│   ├── voiceover_synthesizer.py          # ElevenLabs / Mock synthesizer
│   ├── descript_orchestrator.py          # Descript API & Underlord orchestrator
│   ├── buffer_publisher.py               # LinkedIn social formatter & scheduler
│   └── pipeline.py                       # Master orchestrator
├── tests/                                # Test suite
│   ├── test_quota.py
│   └── test_pipeline.py
├── LINKEDIN_STRATEGY.md                  # LinkedIn profiel optimalisatie & 5 post templates
├── ROADMAP_30_DAYS.md                    # 4-Weken programma naar Descript Expert
├── TRACKER.md                            # Interactieve voortgangs- & KPI-checklist
├── requirements.txt                      # Python dependencies
└── package.json                          # NPM tooling & scripts
```

---

## 📜 Licentie

Gelicentieerd onder de [Apache License 2.0](LICENSE).  
Ontwikkeld door **Philippe Godfroy**.
