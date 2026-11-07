# Underlord Skill: Product Demo Editor

> **Workflow-type:** Herbruikbare Descript Underlord Skill (geïntroduceerd najaar 2026).  
> **Doel:** Transformeert ruwe schermopnames en voice-overs in consistente, professionele software productdemonstraties.

---

## 1. Doelstelling & Scope
Deze Underlord skill automatiseert de montagestappen voor technische softwareprojecten. Het brengt rust in de audio, snijdt aarzelingen weg, accentueert de kernfunctionaliteiten en voegt visuele merkconsistentie toe.

---

## 2. Underlord Prompt Reeks (Stap voor Stap)

Voer de volgende prompts achtereenvolgens in via **Underlord AI** in Descript (of via `descript-api agent --prompt "..."`):

### Stap 1: Audio Sanering & Balans
```text
Underlord, apply Studio Sound to all audio tracks at 85% intensity.
Scan the transcript and automatically remove all filler words ('um', 'uh', 'dus', 'eigenlijk') and shorten all pauses longer than 0.5 seconds to 0.2 seconds.
```

### Stap 2: Scène Indeling & Titels
```text
Analyze the transcript topics and split the timeline into logical scenes (Intro, Problem, Demo Walkthrough, Architecture, Outro).
Add a scene boundary marker at each topic transition.
For each scene, generate a clean, modern lower-third title card with 12px padding, dark translucent background, and white bold typography.
```

### Stap 3: Dynamische Zooms & Visual Focus
```text
Whenever a software feature, code terminal, or button click is mentioned in the voiceover, apply an automatic 15% smooth zoom focused on the active screen region.
Ensure transitions between full view and zoomed view use a 300ms ease-in-out easing curve.
```

### Stap 4: Dynamische Ondertiteling
```text
Add dynamic synchronized captions to the entire video.
Position: bottom-center with 80px bottom margin.
Style: 36pt font, high-contrast white text with subtle dark shadow. Highlight the currently spoken word with our brand accent color (#2563EB).
```

### Stap 5: Outro & Branding
```text
Insert an outro scene at the end of the video: display the GitHub repository name, our website, and a subtle animated 'Subscribe / Connect on LinkedIn' badge.
Fade out background music smoothly over the final 3 seconds.
```

---

## 3. Aanbevolen Video Specificaties
- **Resolutie:** 1080p (1920x1080)
- **Aspect Ratio:** 16:9 Landscape
- **Framerate:** 30 fps of 60 fps
- **Ondertiteling:** Gebrand, geanimeerd
