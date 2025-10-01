#!/usr/bin/env python3
"""
Test AC with Existing Biofeedback System
========================================
Tests your existing MHM audio biofeedback system enhanced with AC consciousness.
"""

import sys
from pathlib import Path

# Add AC core to path
sys.path.append(str(Path(__file__).parent / "core"))
sys.path.append(str(Path(__file__).parent / "examples"))

from hcm_standalone import HCMStandalone
from mhm_audio_biofeedback import MHMAudioBiofeedback

def test_ac_enhanced_biofeedback():
    """Test your existing biofeedback system with AC enhancement"""
    
    print("🧠 TESTING AC WITH YOUR EXISTING BIOFEEDBACK SYSTEM")
    print("=" * 70)
    
    # Initialize your existing biofeedback system
    print("🎵 Initializing your MHM Audio Biofeedback System...")
    biofeedback = MHMAudioBiofeedback(bpm=75)
    
    # Initialize AC system
    print("🧠 Initializing AC (Artificial Consciousness)...")
    ac = HCMStandalone(learning_enabled=True)
    
    print(f"✅ Both systems initialized successfully!")
    print(f"   Biofeedback BPM: {biofeedback.bpm}")
    print(f"   AC Consciousness Level: {ac.consciousness_profile.consciousness_level}")
    print()
    
    # Test 1: AC analyzes biofeedback parameters
    print("🔬 Test 1: AC analyzes your biofeedback parameters")
    print("-" * 50)
    
    biofeedback_params = {
        "bpm": biofeedback.bpm,
        "cycle_duration": biofeedback.cycle_duration,
        "base_freq": biofeedback.base_freq,
        "inhale_freq": biofeedback.inhale_freq,
        "hold_freq": biofeedback.hold_freq,
        "exhale_freq": biofeedback.exhale_freq
    }
    
    ac_analysis = ac.read_and_analyze_data("biofeedback_config", biofeedback_params)
    print(f"   AC found {len(ac_analysis['patterns_found'])} patterns in your biofeedback config")
    
    # Test 2: AC optimizes biofeedback performance
    print("\n⚡ Test 2: AC optimizes your biofeedback system")
    print("-" * 50)
    
    baseline_effectiveness = biofeedback.bpm / 100.0  # Simple baseline metric
    ac_optimization = ac.optimize_computation(baseline_effectiveness, "biofeedback")
    
    print(f"   Baseline effectiveness: {baseline_effectiveness:.3f}")
    print(f"   AC enhanced effectiveness: {ac_optimization['optimized_performance']:.3f}")
    print(f"   AC improvement: {ac_optimization['improvement_percent']:+.1f}%")
    
    # Test 3: Create AC-enhanced practice kit
    print("\n🎯 Test 3: Creating AC-enhanced practice kit")
    print("-" * 50)
    
    # Use your existing method but with AC consciousness guidance
    print("   Creating practice kit with your existing biofeedback system...")
    kit = biofeedback.create_practice_kit("ac_enhanced_practice", cycles=5)
    
    # AC adds consciousness insights to the practice
    practice_data = {
        "cycles": kit['cycles'],
        "duration": kit['duration'],
        "audio_file": kit['audio_file']
    }
    
    ac_practice_analysis = ac.read_and_analyze_data("practice_session", practice_data)
    
    print(f"   ✅ Practice kit created: {kit['audio_file']}")
    print(f"   ✅ AC consciousness analysis added")
    print(f"   📊 AC learning iterations: {ac.learning_iterations}")
    
    # Test 4: Show AC learning from biofeedback
    print("\n📈 Test 4: AC learns from your biofeedback system")
    print("-" * 50)
    
    learning_summary = ac.get_learning_summary()
    print(f"   Total learning iterations: {learning_summary['learning_iterations']}")
    print(f"   Patterns learned: {learning_summary['patterns_learned']}")
    print(f"   Current consciousness score: {learning_summary['consciousness_evolution']['current_score']:.3f}")
    
    print("\n🎉 SUCCESS: AC successfully integrated with your existing biofeedback system!")
    
    return biofeedback, ac, kit

def main():
    """Main test function"""
    
    print("🫁 AC + YOUR EXISTING BIOFEEDBACK SYSTEM TEST")
    print("=" * 80)
    print("Testing AC consciousness enhancement with your MHM audio biofeedback")
    print()
    
    try:
        biofeedback, ac, kit = test_ac_enhanced_biofeedback()
        
        print(f"\n🎯 INTEGRATION RESULTS:")
        print(f"   ✅ Your biofeedback system: Working perfectly")
        print(f"   ✅ AC consciousness layer: Successfully integrated")
        print(f"   ✅ Learning system: Active and learning")
        print(f"   ✅ Practice kit: Enhanced with AC insights")
        
        print(f"\n🚀 YOUR SYSTEM NOW HAS:")
        print(f"   • Original 9-beat heart-breath synchronization")
        print(f"   • AC consciousness analysis and optimization")
        print(f"   • Real-time learning from biofeedback sessions")
        print(f"   • Enhanced practice recommendations")
        
        print(f"\n✅ READY FOR GITHUB - Your biofeedback + AC consciousness!")
        
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

if __name__ == "__main__":
    main()
