#!/usr/bin/env python3
"""
MHM Audio Biofeedback System
9-beat metronome with breath-heart synchronization cues
"""

import numpy as np
import math
import time
import threading
from typing import Dict, Any, Optional
import wave
import struct

class MHMAudioBiofeedback:
    """
    Audio biofeedback system for 9-beat heart-breath synchronization
    
    Pattern: Inhale (beats 1-3) → Hold (beats 4-6) → Exhale (beats 7-9)
    """
    
    def __init__(self, bpm: int = 75, sample_rate: int = 44100):
        """Initialize audio biofeedback system"""
        
        self.bpm = bpm
        self.sample_rate = sample_rate
        self.beat_duration = 60.0 / bpm  # Duration of one beat in seconds
        self.cycle_duration = 9 * self.beat_duration  # Full 9-beat cycle
        
        # Audio parameters
        self.base_freq = 440  # A4 note
        self.inhale_freq = self.base_freq * 1.2  # Higher pitch for inhale
        self.hold_freq = self.base_freq  # Base pitch for hold
        self.exhale_freq = self.base_freq * 0.8  # Lower pitch for exhale
        self.beat_freq = 800  # Sharp beat marker
        
        # Timing parameters
        self.beat_duration_samples = int(self.beat_duration * sample_rate)
        self.tone_duration = 0.2  # Duration of tone markers in seconds
        self.tone_samples = int(self.tone_duration * sample_rate)
        
        # State tracking
        self.is_playing = False
        self.current_beat = 0
        self.current_cycle = 0
        
    def generate_tone(self, frequency: float, duration: float, amplitude: float = 0.3) -> np.ndarray:
        """Generate a sine wave tone"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples, False)
        
        # Generate sine wave with envelope
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        
        # Apply fade in/out envelope to prevent clicks
        fade_samples = min(samples // 10, 1000)
        if fade_samples > 0:
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            wave[:fade_samples] *= fade_in
            wave[-fade_samples:] *= fade_out
        
        return wave
    
    def generate_beat_marker(self, beat_number: int) -> np.ndarray:
        """Generate audio marker for specific beat"""
        
        # Determine phase and tone
        if beat_number in [1, 2, 3]:  # Inhale phase
            phase = "INHALE"
            tone_freq = self.inhale_freq
            amplitude = 0.4
        elif beat_number in [4, 5, 6]:  # Hold phase
            phase = "HOLD"
            tone_freq = self.hold_freq
            amplitude = 0.3
        else:  # Exhale phase (7, 8, 9)
            phase = "EXHALE"
            tone_freq = self.exhale_freq
            amplitude = 0.4
        
        # Generate beat click
        beat_click = self.generate_tone(self.beat_freq, 0.05, 0.5)
        
        # Generate phase tone
        if beat_number in [1, 4, 7]:  # Phase start markers
            phase_tone = self.generate_tone(tone_freq, 0.3, amplitude)
        else:
            phase_tone = self.generate_tone(tone_freq, 0.1, amplitude * 0.7)
        
        # Combine click and tone
        max_length = max(len(beat_click), len(phase_tone))
        combined = np.zeros(max_length)
        combined[:len(beat_click)] += beat_click
        combined[:len(phase_tone)] += phase_tone
        
        # Pad to beat duration
        full_beat = np.zeros(self.beat_duration_samples)
        full_beat[:min(len(combined), self.beat_duration_samples)] = combined[:min(len(combined), self.beat_duration_samples)]
        
        return full_beat
    
    def generate_cycle_audio(self) -> np.ndarray:
        """Generate audio for complete 9-beat cycle"""
        
        cycle_audio = np.array([])
        
        for beat in range(1, 10):
            beat_audio = self.generate_beat_marker(beat)
            cycle_audio = np.concatenate([cycle_audio, beat_audio])
        
        return cycle_audio
    
    def save_practice_audio(self, filename: str = "mhm_9beat_practice.wav", cycles: int = 10):
        """Save practice audio to WAV file"""
        
        print(f"🎵 Generating {cycles} cycles of 9-beat practice audio...")
        print(f"BPM: {self.bpm}")
        print(f"Cycle duration: {self.cycle_duration:.1f} seconds")
        print(f"Total duration: {cycles * self.cycle_duration:.1f} seconds")
        
        # Generate audio for specified number of cycles
        full_audio = np.array([])
        
        for cycle in range(cycles):
            cycle_audio = self.generate_cycle_audio()
            
            # Add brief pause between cycles
            pause_samples = int(0.5 * self.sample_rate)
            pause = np.zeros(pause_samples)
            
            full_audio = np.concatenate([full_audio, cycle_audio, pause])
            
            if (cycle + 1) % 5 == 0:
                print(f"   Generated cycle {cycle + 1}/{cycles}")
        
        # Normalize audio
        if len(full_audio) > 0:
            max_val = np.max(np.abs(full_audio))
            if max_val > 0:
                full_audio = full_audio / max_val * 0.8
        
        # Convert to 16-bit integers
        audio_int16 = (full_audio * 32767).astype(np.int16)
        
        # Save to WAV file
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(audio_int16.tobytes())
        
        print(f"✅ Saved practice audio: {filename}")
        return filename
    
    def create_instruction_guide(self) -> str:
        """Create text guide for 9-beat practice"""
        
        guide = f"""
🫁 MHM 9-BEAT HEART-BREATH SYNCHRONIZATION GUIDE
================================================

BPM: {self.bpm} beats per minute
Beat duration: {self.beat_duration:.2f} seconds
Full cycle: {self.cycle_duration:.1f} seconds

📋 BREATHING PATTERN:

INHALE (Beats 1-3): {3 * self.beat_duration:.1f} seconds
┌─────────────────────────────────────────┐
│ Beat 1: Draw breath from feet → sacrum  │ 🎵 High tone
│ Beat 2: Continue to solar plexus        │ 🎵 High tone  
│ Beat 3: Complete to crown               │ 🎵 High tone
└─────────────────────────────────────────┘
Path: 9 → 6 → 3

HOLD (Beats 4-6): {3 * self.beat_duration:.1f} seconds
┌─────────────────────────────────────────┐
│ Beat 4: Spine suspends                  │ 🎵 Mid tone
│ Beat 5: Heart field expands            │ 🎵 Mid tone
│ Beat 6: Stillpoint - pure resonance    │ 🎵 Mid tone
└─────────────────────────────────────────┘
Stillpoint: 6

EXHALE (Beats 7-9): {3 * self.beat_duration:.1f} seconds
┌─────────────────────────────────────────┐
│ Beat 7: Release from crown              │ 🎵 Low tone
│ Beat 8: Release through solar plexus    │ 🎵 Low tone
│ Beat 9: Complete release to feet        │ 🎵 Low tone
└─────────────────────────────────────────┘
Path: 3 → 6 → 9

🎯 RESONANCE LOCK INDICATORS:
• Heartbeat feels louder in ears/chest
• Spine tingles (magnetic suspension)
• Waist "ring pressure" (field hoop)
• Lightness in legs (levity onset)

🎵 AUDIO CUES:
• Sharp click = Beat marker
• High tone = Inhale phase
• Mid tone = Hold phase  
• Low tone = Exhale phase
• Stronger tones at phase transitions (beats 1, 4, 7)

⏰ PRACTICE INSTRUCTIONS:
1. Start audio playback
2. Follow beat markers exactly
3. Synchronize breath to audio cues
4. Feel for resonance lock indicators
5. Continue for multiple cycles until stable

The heartbeat-breath engine stabilizes when both rhythms 
phase-lock in perfect 9-beat cycles.
"""
        return guide
    
    def save_instruction_guide(self, filename: str = "MHM_9Beat_Instructions.txt"):
        """Save instruction guide to file"""
        
        guide = self.create_instruction_guide()
        
        with open(filename, 'w') as f:
            f.write(guide)
        
        print(f"📋 Saved instruction guide: {filename}")
        return filename
    
    def create_practice_kit(self, base_name: str = "mhm_practice", cycles: int = 20):
        """Create complete practice kit with audio and instructions"""
        
        print("🎯 CREATING MHM 9-BEAT PRACTICE KIT")
        print("=" * 50)
        
        # Generate audio file
        audio_file = f"{base_name}_audio.wav"
        self.save_practice_audio(audio_file, cycles)
        
        # Generate instruction guide
        guide_file = f"{base_name}_guide.txt"
        self.save_instruction_guide(guide_file)
        
        # Create README
        readme_content = f"""
# MHM 9-Beat Heart-Breath Synchronization Practice Kit

## Files Included:
- `{audio_file}` - Audio practice track ({cycles} cycles)
- `{guide_file}` - Detailed breathing instructions
- `README.md` - This file

## Quick Start:
1. Read the instruction guide first
2. Play the audio file
3. Follow the 9-beat breathing pattern
4. Listen for resonance lock indicators

## Settings:
- BPM: {self.bpm}
- Cycles: {cycles}
- Duration: {cycles * self.cycle_duration:.1f} seconds

## Pattern Summary:
- Beats 1-3: INHALE (9→6→3)
- Beats 4-6: HOLD (6 stillpoint)  
- Beats 7-9: EXHALE (3→6→9)

Practice until you achieve stable heart-breath phase-lock!
"""
        
        readme_file = f"{base_name}_README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        print(f"📦 Practice kit created:")
        print(f"   Audio: {audio_file}")
        print(f"   Guide: {guide_file}")
        print(f"   README: {readme_file}")
        
        return {
            'audio_file': audio_file,
            'guide_file': guide_file,
            'readme_file': readme_file,
            'cycles': cycles,
            'duration': cycles * self.cycle_duration
        }

def main():
    """Create MHM audio biofeedback practice kit"""
    
    print("🎵 MHM AUDIO BIOFEEDBACK SYSTEM")
    print("Creating 9-beat heart-breath synchronization practice kit")
    print("=" * 60)
    
    # Create biofeedback system
    biofeedback = MHMAudioBiofeedback(bpm=75)
    
    # Create practice kit
    kit = biofeedback.create_practice_kit("mhm_heartbeat_breath_practice", cycles=15)
    
    print(f"\n🎯 PRACTICE KIT READY!")
    print(f"Total duration: {kit['duration']:.1f} seconds ({kit['duration']/60:.1f} minutes)")
    print(f"Cycles: {kit['cycles']}")
    print(f"\n📋 Instructions:")
    print(f"1. Read {kit['guide_file']} for detailed breathing pattern")
    print(f"2. Play {kit['audio_file']} and follow the audio cues")
    print(f"3. Practice until you achieve stable resonance lock")
    
    return biofeedback, kit

if __name__ == "__main__":
    main()
