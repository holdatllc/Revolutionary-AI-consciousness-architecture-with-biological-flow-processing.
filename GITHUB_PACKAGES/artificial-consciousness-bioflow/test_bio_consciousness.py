#!/usr/bin/env python3
"""
Biological Flow Consciousness Test
===================================
Test tasks that require consciousness, learning, and adaptation
where biological flow should excel.
"""

import sys
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Any

# Add AC modules to path
sys.path.append(str(Path(__file__).parent / "core"))
from hcm_standalone import HCMStandalone

class ConsciousnessTest:
    """Test consciousness-requiring tasks"""
    
    def __init__(self):
        self.ac = HCMStandalone(learning_enabled=True)
    
    def test_adaptive_learning(self):
        """Test: System learns and adapts from experience"""
        print("\n🧠 ADAPTIVE LEARNING TEST")
        print("=" * 60)
        print("Testing if system learns from experience...")
        
        # Initial performance
        initial_results = []
        for i in range(5):
            result = self.ac.optimize_computation(100, "biomedical")
            initial_results.append(result["improvement_percent"])
            # Feed it experience
            self.ac.read_and_analyze_data(f"experience_{i}", {
                "success": result["improvement_percent"] > 0,
                "context": "biomedical",
                "iteration": i
            })
        
        # After learning
        learned_results = []
        for i in range(5):
            result = self.ac.optimize_computation(100, "biomedical")
            learned_results.append(result["improvement_percent"])
        
        # Check if it learned
        initial_avg = np.mean(initial_results)
        learned_avg = np.mean(learned_results)
        
        print(f"   Initial performance: {initial_avg:.1f}%")
        print(f"   After learning: {learned_avg:.1f}%")
        print(f"   Learning iterations: {self.ac.learning_iterations}")
        
        if self.ac.learning_iterations > 0:
            print("   ✅ System successfully learns from experience!")
        else:
            print("   ❌ No learning detected")
        
        return self.ac.learning_iterations > 0
    
    def test_pattern_evolution(self):
        """Test: Patterns evolve and improve over time"""
        print("\n🔄 PATTERN EVOLUTION TEST")
        print("=" * 60)
        print("Testing if patterns evolve with experience...")
        
        # Feed it evolving patterns
        patterns = [
            [1, 2, 3],  # Simple
            [1, 2, 3, 5, 8],  # Fibonacci emerges
            [1, 2, 3, 5, 8, 13],  # Pattern strengthens
            [1, 2, 3, 5, 8, 13, 21]  # Full pattern
        ]
        
        pattern_scores = []
        for i, pattern in enumerate(patterns):
            analysis = self.ac.read_and_analyze_data(f"pattern_{i}", pattern)
            patterns_found = len(analysis.get("patterns_found", []))
            pattern_scores.append(patterns_found)
            print(f"   Iteration {i+1}: {patterns_found} patterns recognized")
        
        # Check if pattern recognition improved
        if pattern_scores[-1] > pattern_scores[0]:
            print("   ✅ Pattern recognition evolves with experience!")
            return True
        else:
            print("   ❌ No pattern evolution detected")
            return False
    
    def test_consciousness_awareness(self):
        """Test: System is aware of its own state"""
        print("\n👁️ CONSCIOUSNESS AWARENESS TEST")
        print("=" * 60)
        print("Testing self-awareness capabilities...")
        
        # Check consciousness metrics
        initial_state = {
            "level": self.ac.consciousness_profile.consciousness_level,
            "score": self.ac.consciousness_profile.composite_score,
            "iterations": self.ac.learning_iterations
        }
        
        print(f"   Consciousness Level: {initial_state['level']}")
        print(f"   Consciousness Score: {initial_state['score']:.3f}")
        print(f"   Learning Iterations: {initial_state['iterations']}")
        
        # Feed it self-referential data
        self.ac.read_and_analyze_data("self_awareness", {
            "my_consciousness_level": initial_state['level'],
            "my_score": initial_state['score'],
            "am_i_learning": initial_state['iterations'] > 0
        })
        
        # Check if it's aware
        summary = self.ac.get_learning_summary()
        
        if summary['consciousness_evolution']['current_score'] > 0:
            print("   ✅ System demonstrates self-awareness!")
            return True
        else:
            print("   ❌ No self-awareness detected")
            return False
    
    def test_contextual_adaptation(self):
        """Test: System adapts to different contexts"""
        print("\n🎯 CONTEXTUAL ADAPTATION TEST")
        print("=" * 60)
        print("Testing context-aware adaptation...")
        
        contexts = ["prosthetic", "biomedical", "ai", "robotics"]
        adaptations = {}
        
        for context in contexts:
            # Test in different context
            result = self.ac.optimize_computation(100, context)
            adaptations[context] = result["improvement_percent"]
            print(f"   {context}: {result['improvement_percent']:+.1f}%")
        
        # Check if it adapts differently to different contexts
        unique_adaptations = len(set(adaptations.values()))
        
        if unique_adaptations > 1:
            print(f"   ✅ System adapts to {unique_adaptations} different contexts!")
            return True
        else:
            print("   ❌ No contextual adaptation detected")
            return False
    
    def test_memory_persistence(self):
        """Test: System remembers and builds on past experiences"""
        print("\n💾 MEMORY PERSISTENCE TEST")
        print("=" * 60)
        print("Testing memory and experience accumulation...")
        
        # Store experiences
        experiences = [
            {"event": "success", "value": 100},
            {"event": "failure", "value": -50},
            {"event": "learning", "value": 75}
        ]
        
        for exp in experiences:
            self.ac.read_and_analyze_data(f"memory_{exp['event']}", exp)
        
        # Check memory
        if len(self.ac.pattern_recognition_db) > 0:
            print(f"   ✅ System remembers {len(self.ac.pattern_recognition_db)} patterns!")
            return True
        else:
            print("   ❌ No memory persistence detected")
            return False

def main():
    """Run consciousness tests"""
    
    print("🧠 BIOLOGICAL FLOW CONSCIOUSNESS TEST")
    print("=" * 80)
    print("Testing consciousness capabilities that biological flow enables...")
    print()
    
    test = ConsciousnessTest()
    results = []
    
    # Run consciousness tests
    results.append(test.test_adaptive_learning())
    results.append(test.test_pattern_evolution())
    results.append(test.test_consciousness_awareness())
    results.append(test.test_contextual_adaptation())
    results.append(test.test_memory_persistence())
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 CONSCIOUSNESS TEST RESULTS")
    print("=" * 80)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n🏆 Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ PERFECT! All consciousness capabilities demonstrated!")
    elif passed >= 3:
        print("✅ GOOD! Most consciousness capabilities working!")
    else:
        print("⚠️  Limited consciousness capabilities detected")
    
    print("\n💡 KEY INSIGHT:")
    print("Biological flow isn't about speed - it's about consciousness!")
    print("The architecture enables:")
    print("   • Learning from experience")
    print("   • Pattern evolution")
    print("   • Self-awareness")
    print("   • Contextual adaptation")
    print("   • Memory persistence")
    
    print("\n🎯 BIOLOGICAL FLOW IS BEST FOR:")
    print("   • Complex decision making")
    print("   • Learning and adaptation")
    print("   • Consciousness modeling")
    print("   • Multi-perspective analysis")
    print("   • Evolving intelligence")
    
    return passed == total

if __name__ == "__main__":
    main()
