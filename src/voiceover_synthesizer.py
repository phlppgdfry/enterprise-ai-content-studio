"""Voiceover Synthesizer.

Connects with ElevenLabs API to generate realistic speech audio.
Includes mock / dry-run speech generation for free-tier users to preserve API credits.
"""

from dataclasses import dataclass
import os
from pathlib import Path
from typing import Optional
import wave


@dataclass
class VoiceoverResult:
    audio_path: Path
    character_count: int
    duration_estimate_sec: float
    is_simulated: bool
    voice_id: str


class VoiceoverSynthesizer:
    """Generates audio voiceovers via ElevenLabs or simulation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Rachel
        output_dir: Optional[Path] = None,
    ):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = voice_id
        self.output_dir = output_dir or Path("output/audio")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def synthesize(
        self,
        text: str,
        filename_prefix: str = "voiceover",
        dry_run: bool = False,
    ) -> VoiceoverResult:
        """Generates audio for given text.

        If dry_run is True or no API key is provided, generates a simulated audio file
        so downstream Descript pipelines can continue testing without consuming credits.
        """
        char_count = len(text)
        # Average reading rate: ~15 characters per second (150 words/min)
        est_duration = max(2.0, char_count / 15.0)

        out_file = self.output_dir / f"{filename_prefix}.mp3"
        sim_wav_file = self.output_dir / f"{filename_prefix}.wav"

        if dry_run or not self.api_key:
            # Generate a valid lightweight silent/beeping WAV file for pipeline testing
            self._create_mock_audio_file(sim_wav_file, est_duration)
            return VoiceoverResult(
                audio_path=sim_wav_file,
                character_count=char_count,
                duration_estimate_sec=est_duration,
                is_simulated=True,
                voice_id=self.voice_id,
            )

        # Real ElevenLabs API call
        try:
            import requests

            url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key,
            }
            payload = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                },
            }
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
            if resp.status_code == 200:
                out_file.write_bytes(resp.content)
                return VoiceoverResult(
                    audio_path=out_file,
                    character_count=char_count,
                    duration_estimate_sec=est_duration,
                    is_simulated=False,
                    voice_id=self.voice_id,
                )
            else:
                # API error, fall back to simulation
                self._create_mock_audio_file(sim_wav_file, est_duration)
                return VoiceoverResult(
                    audio_path=sim_wav_file,
                    character_count=char_count,
                    duration_estimate_sec=est_duration,
                    is_simulated=True,
                    voice_id=self.voice_id,
                )
        except Exception:
            self._create_mock_audio_file(sim_wav_file, est_duration)
            return VoiceoverResult(
                audio_path=sim_wav_file,
                character_count=char_count,
                duration_estimate_sec=est_duration,
                is_simulated=True,
                voice_id=self.voice_id,
            )

    def _create_mock_audio_file(self, target_path: Path, duration_sec: float) -> None:
        """Creates a minimal valid PCM WAV file for mock testing."""
        sample_rate = 16000
        num_samples = int(sample_rate * min(duration_sec, 10.0))  # cap size
        with wave.open(str(target_path), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            # 0.1s beep tone + silence
            data = bytearray(num_samples * 2)
            wf.writeframes(bytes(data))
