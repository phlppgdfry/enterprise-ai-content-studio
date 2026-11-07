# Underlord Skill: Multilingual Content Workflow

> **Workflow-type:** Herbruikbare Descript Underlord Skill.  
> **Doel:** Zet één Nederlandstalige bronvideo om in gesynchroniseerde Engelse en Franse versies met behulp van AI vertaling, dubbing en meertalige ondertitels.

---

## 1. Waarom deze workflow?
Door je technische softwarevideo's in meerdere talen aan te bieden, vergroot je je internationale bereik exponentieel. Descript kan een transcript vertalen, AI-spraak opnieuw genereren en de visuele timings automatisch matchen.

---

## 2. Underlord Prompt Reeks

### Stap 1: Nauwkeurige Bron Transcriptie Verificatie
```text
Underlord, review the Dutch transcript of this composition.
Ensure technical jargon, repository names, and English terminology (e.g. 'CLI', 'OAuth', 'FastAPI', 'pipeline') are correctly spelled and capitalized.
Lock timeline marker positions for key screen transitions.
```

### Stap 2: Dupliceren naar Doeltalen
```text
Duplicate this composition into two new compositions:
1. 'Composition - EN (English)'
2. 'Composition - FR (Français)'
```

### Stap 3: Vertalen met Behoud van Technische Context (EN & FR)
```text
[In English Composition]:
Translate the Dutch transcript into professional American English.
Tone: crisp, technical, confident. Adapt Dutch expressions to idiomatic developer language.

[In French Composition]:
Translate the Dutch transcript into professional French (informatique / cloud).
Tone: précis et professionnel.
```

### Stap 4: AI Voice Dubbing & Speech Matching
```text
Generate localized voiceovers using Descript AI Speech for the translated scripts.
Adjust speech pacing and apply time-compression (up to 1.15x) if the translated sentences require more spoken time than the original footage, ensuring visual screen events remain synchronized with the voiceover.
```

### Stap 5: Gelokaliseerde Ondertitels & Layout
```text
Apply localized captions in the target language.
Verify that sentence splits occur on natural pause points.
Export composition preview and verify lip-sync / screen alignment.
```
