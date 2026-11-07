# Project 4: AI Content Repurposing Engine

> **Doel:** Leren hoe je 1 lange bronvideo (5 min) efficiënt omzet in 5 verschillende geoptimaliseerde contentformats.

---

## 🎯 De Repurposing Matrix

| Output Format | Doelplatform | Doelduur | Aspect Ratio | Belangrijkste Eigenschap |
|---|---|---|---|---|
| **LinkedIn Clip** | LinkedIn Feed | 60 sec | 1:1 of 16:9 | Focus op business value, ondertiteling groot |
| **YouTube Short** | YouTube Shorts | 30-45 sec | 9:16 Verticaal | Zeer snelle hook in eerste 3 seconden |
| **Instagram Reel** | Instagram & TikTok | 30 sec | 9:16 Verticaal | Energieke achtergrondmuziek, punchy captions |
| **Executive Summary** | Pitch / Website | 2 min | 16:9 Landscape | Hoofdlijnen & architectuur overzicht |
| **Master Walkthrough** | Documentatie / Docs | 5 min | 16:9 Landscape | Volledige diepgang en stap-voor-stap uitleg |

---

## 🛠️ Gebruikte Descript-functies (Badge Activators)
- [x] **Clip-extractie uit transcript**: Tekst markeren en direct omzetten naar een nieuwe compositie.
- [x] **Aspect ratio conversie (Canvas resizing)**: 16:9 naar 9:16 en 1:1 met behulp van templates.
- [x] **Auto-framing & face tracking**: De camera automatisch laten focussen op het actieve element in een verticaal kader.
- [x] **Social templates & layouts**: Banners bovenaan ('HOE HET WERKT'), captions in het midden.
- [x] **Batch export**: Meerdere composities tegelijkertijd renderen.

---

## 📋 Stappenplan

### Stap 1: Mastervideo Opladen (10 min)
1. Importeer een 5-minuten demo van je project in Descript.
2. Zorg voor automatische transcriptie en filler-word opschoning.

### Stap 2: Highlights Selecteren (15 min)
1. Lees het transcript door en markeer 2 tot 3 krachtige secties van 45-60 seconden.
2. Klik met de rechtermuisknop op de geselecteerde tekst en kies **Duplicate to → New composition**.
3. Noem de eerste compositie `LinkedIn Clip 60s` en de tweede `Short 30s`.

### Stap 3: Formaten Converteren (15 min)
1. Open de `Short 30s` compositie.
2. Klik linksboven op de canvas-instelling en kies **Portrait (9:16)**.
3. Gebruik de [LinkedIn Clips Extractor skill](../../underlord-skills/linkedin-clips-extractor.md) om een viraal sjabloon toe te passen.

### Stap 4: Exporteren (10 min)
1. Exporteer de verschillende formaten.
2. Vink Project 4 af in [TRACKER.md](../../TRACKER.md)!
