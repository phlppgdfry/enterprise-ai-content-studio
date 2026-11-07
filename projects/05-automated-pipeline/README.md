# Project 5: Autonomous Enterprise AI Content Studio

> **Doel:** De kroon op je portfolio — een end-to-end geautomatiseerde pipeline die GitHub releases omzet in videodemo's en LinkedIn-posts. Ontgrendelt de weg naar **🥇 Descript Expert**.

---

## 🏗️ De Volledige Workflow Architectuur

```text
       ┌────────────────────────┐
       │     GitHub Release     │  (git tag push of commit analyse)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │   AI Release Parser    │  (features, fixes en context filteren)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  AI Script Generator   │  (hooks, visuele cues & voiceover)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ ElevenLabs Synthesizer │  (studiokwaliteit spraakaudio)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  Descript Orchestrator │  (Underlord AI montage, Studio Sound,
       │  & CLI / MCP Engine    │   filler words weg, captions & publicatie)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ Human Quality Approval │  (kwaliteitscontrole & preview)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │    Buffer Scheduler    │  (LinkedIn post inplannen & publiceren)
       └────────────────────────┘
```

---

## 🛡️ Slim Quota-beheer (Free Plan Optimalisatie)

Omdat de gratis accounts van Descript (60 min transcriptie/maand) en ElevenLabs (10.000 karakters/maand) limieten hebben, bevat deze studio een ingebouwde **Quota Guard**:

1. **Dry-Run / Simulatiemodus (`python3 src/cli.py simulate`)**:
   - Voert de complete logica uit (release analyse, scriptopbouw, audio-mock, Descript mock, Buffer payload) **zonder ook maar één API-tegoed te verbruiken**.
   - Perfect om pipelines, scripts en integraties te testen en te demonstreren op GitHub.
2. **Capaciteitscontrole vooraf**:
   - Controleert vóór elke run of er voldoende minuten/karakters over zijn.
   - Zo niet: schakelt automatisch over naar simulatiemodus met een duidelijke melding.
3. **Automatische Maandelijkse Reset**:
   - Berekent automatisch wanneer je nieuwe bundel ingaat (elke 1e van de maand).
   - Houdt de historische activiteit netjes bij in `quota_state.json`.

---

## 🚀 Hoe voer je dit uit?

```bash
# 1. Controleer je huidige tegoed en volgende resetdatum
python3 src/cli.py quota

# 2. Test een veilige simulatie (0 credits verbruikt)
python3 src/cli.py simulate

# 3. Voer een echte run uit voor een LinkedIn 60s video
python3 src/cli.py run linkedin-60s

# 4. Voer een verticale 30s short uit
python3 src/cli.py run short-30s
```

Vink Project 5 af in [TRACKER.md](../../TRACKER.md)!
