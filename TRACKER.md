# 📊 Descript Expert & Portfolio Voortgangs-Tracker

> Gebruik dit document om je dagelijkse voortgang, voltooide functies, projectmijlpalen en LinkedIn-certificeringen bij te houden.

---

## 🎖️ Officiële Certificeringsstatus (LinkedIn)

Verbind je Descript-account via **Settings → Connections** om badges automatisch te synchroniseren.

- [ ] 🥉 **Niveau 1: Proficient** (Basis bewerkings- en opnameactiviteit)
- [ ] 🥈 **Niveau 2: Advanced** (Geavanceerde AI-functies, multi-track, Underlord)
- [ ] 🥇 **Niveau 3: Expert** (Meertalig, repurposing, API/CLI automatisering en consistente productie)

---

## 📈 30-Dagen KPI Scorecard

| KPI | Doelstelling | Huidige Score | Status |
|---|---|---|---|
| **Voltooide Video's** | 5 | 0 / 5 | ⏳ In uitvoering |
| **Professionele Productdemo's** | 2 | 0 / 2 | ⏳ In uitvoering |
| **Gebruikte Descript-functies** | 12+ | 0 / 14 | ⏳ In uitvoering |
| **Meertalige Video's** | 1 project in 3 talen | 0 / 3 | ⏳ In uitvoering |
| **Herbruikbare Underlord Skills** | 3 | 3 / 3 | ✅ Gedefinieerd |
| **Werkende API / CLI Automatiseringen** | 1 | 1 / 1 | ✅ Gereed in `src/` |
| **Gedocumenteerd GitHub-project** | 1 | 1 / 1 | ✅ Gereed |
| **LinkedIn Certificering Geclaimd** | Hoogste niveau | Nog te verbinden | ⏳ Wacht op feature volume |

---

## 🛠️ Descript Feature Matrix (14 Kernfuncties)

Vink elke functie af zodra je deze minimaal één keer hebt toegepast in Descript:

- [ ] **1. Screen Recording** (Scherm & microfoon direct opnemen)
- [ ] **2. Automatische Transcriptie** (Spraak naar tekst)
- [ ] **3. Tekst-gebaseerd Monteren** (Woorden wissen = video knippen)
- [ ] **4. Filler Words Verwijderen** (1-klik opschonen van 'eh' en stiltes)
- [ ] **5. Studio Sound** (AI audio-isolatie en kristalhelder stemgeluid)
- [ ] **6. Scènes Maken met `/`** (Scènegrenzen en transities)
- [ ] **7. Dynamische Ondertitels (Captions)** (Met actieve woordkleur)
- [ ] **8. Underlord AI Co-editor** (Natuurlijke taal bewerkingsprompts)
- [ ] **9. AI Speech / Overdub** (Stemcorrectie en voice cloning)
- [ ] **10. Automatische B-roll Invoegen** (Stockmateriaal & code overlays)
- [ ] **11. Multi-track & PiP Layouts** (Webcam overlay en split screens)
- [ ] **12. Aspect Ratio Resizing** (16:9 naar 9:16 en 1:1)
- [ ] **13. AI Transcript Vertaling & Dubbing** (Meertalige output)
- [ ] **14. CLI & MCP Automatisering** (`descript-api` & `https://api.descript.com/v2/mcp`)

---

## 🚀 De 5 Portfolio Mijlpalen

- [ ] **Project 1:** [Professional AI Video Editing (60-90 sec)](projects/01-professional-editing/)
  - *Link naar export/video:* `...`
  - *LinkedIn post geplaatst:* `[Ja / Nee]`
- [ ] **Project 2:** [AI Product Demo met Underlord (2-3 min)](projects/02-ai-product-demo/)
  - *Link naar export/video:* `...`
  - *LinkedIn post geplaatst:* `[Ja / Nee]`
- [ ] **Project 3:** [Meertalige AI Content (NL, EN, FR)](projects/03-multilingual-content/)
  - *Link naar export/video:* `...`
  - *LinkedIn post geplaatst:* `[Ja / Nee]`
- [ ] **Project 4:** [Content Repurposing (5 formats uit 1 master)](projects/04-content-repurposing/)
  - *Link naar export/video:* `...`
  - *LinkedIn post geplaatst:* `[Ja / Nee]`
- [ ] **Project 5:** [Autonomous Enterprise Content Studio](projects/05-automated-pipeline/)
  - *Link naar export/video:* `...`
  - *LinkedIn post geplaatst:* `[Ja / Nee]`

---

## 🛡️ Maandelijkse Free-Tier Quota & Rollover Status

Voer `python3 src/cli.py quota` uit om de actuele stand uit `quota_state.json` te synchroniseren:

```json
{
  "descript_minutes_remaining": 60.0,
  "elevenlabs_chars_remaining": 10000,
  "next_monthly_reset": "Elke 1e van de kalendermaand",
  "safe_simulation_mode": true
}
```

> **Tip:** Zit je tegen je limiet van de gratis bundel aan? Schakel over naar de simulatiemodus via `python3 src/cli.py simulate` om pipelines en scripts foutloos te blijven testen zonder tegoed te verspillen. Na de maandelijkse reset werk je direct weer verder met echte exports!
