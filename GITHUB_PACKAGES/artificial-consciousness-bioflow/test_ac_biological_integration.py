#!/usr/bin/env python3
"""
Test AC + Biological Flow Integration
======================================
Combines AC consciousness with biological flow architecture.
Information flows like blood, gathering insights as it travels.
"""

import sys
import time
import numpy as np
from pathlib import Path
from typing import Dict, Any

# Add AC modules to path
sys.path.append(str(Path(__file__).parent / "core"))
from hcm_standalone import HCMStandalone
from ac_biological_flow import ACBiologicalFlow, InformationPacket

class ACBiologicalIntegration:
    """
    Integration of AC consciousness with biological flow.
    Information flows like blood through the AI brain.
    """
    
    def __init__(self):
        # Initialize AC consciousness
        self.ac = HCMStandalone(learning_enabled=True)
        
        # Initialize biological flow system
        self.bio_flow = ACBiologicalFlow(heart_rate=75)
        
        # Connect AC to organs
        self._connect_ac_to_organs()
        
        # System state
        self.processing_history = []
        
    def _connect_ac_to_organs(self):
        """Connect AC consciousness to biological organs"""
        
        # Override organ processing to use AC
        original_brain_process = self.bio_flow.organs["brain"].process
        original_heart_process = self.bio_flow.organs["heart"].process
        
        def ac_brain_process(organ):
            """AC-enhanced brain processing"""
            if organ.processing_queue:
                packet = organ.processing_queue.popleft()
                
                # Use AC to process the information
                ac_result = self.ac.optimize_computation(
                    len(str(packet.data)), "ai"
                )
                
                # Learn from the data
                self.ac.read_and_analyze_data("brain_process", packet.data)
                
                # Add AC insights as nutrients
                packet.nutrients_collected.append(f"ac_reasoning_{ac_result['improvement_percent']:.1f}%")
                packet.nutrients_collected.append(f"consciousness_{self.ac.consciousness_profile.consciousness_level}")
                
                organ.processed.append(packet)
        
        def ac_heart_process(organ):
            """AC-enhanced heart processing"""
            if organ.processing_queue:
                packet = organ.processing_queue.popleft()
                
                # Use AC for emotional/rhythm processing
                ac_result = self.ac.optimize_computation(
                    len(str(packet.data)), "biomedical"
                )
                
                # Add rhythm and emotional insights
                packet.nutrients_collected.append(f"rhythm_coherence_{ac_result['improvement_percent']:.1f}%")
                packet.nutrients_collected.append("emotional_balance")
                
                organ.processed.append(packet)
        
        # Replace organ processing with AC-enhanced versions
        self.bio_flow.organs["brain"].process = lambda: ac_brain_process(self.bio_flow.organs["brain"])
        self.bio_flow.organs["heart"].process = lambda: ac_heart_process(self.bio_flow.organs["heart"])
    
    def process_with_biological_flow(self, data: Any, destination: str = "brain") -> Dict:
        """
        Process information through biological flow with AC consciousness
        
        Args:
            data: Information to process
            destination: Target processing center
            
        Returns:
            Processed result with insights gathered during flow
        """
        
        print(f"\n💉 Injecting: {str(data)[:50]}...")
        
        # Inject information into bloodstream
        packet = self.bio_flow.inject_information(data, destination)
        
        # Let it flow through the system (multiple heartbeats)
        print("🫀 Pumping through consciousness...")
        
        # Process through organs during heartbeats
        for beat in range(10):  # 10 heartbeats
            # Manually trigger organ processing
            for organ in self.bio_flow.organs.values():
                organ.process()
            
            # Check if packet has gathered enough insights
            if len(packet.nutrients_collected) >= 3:
                break
            
            time.sleep(self.bio_flow.beat_interval)
        
        # Synthesize answer from collected nutrients
        answer = self.bio_flow._synthesize_answer(packet)
        
        # Add AC learning summary
        answer["ac_learning"] = {
            "iterations": self.ac.learning_iterations,
            "consciousness_score": self.ac.consciousness_profile.composite_score,
            "patterns_found": len(self.ac.pattern_recognition_db)
        }
        
        self.processing_history.append(answer)
        
        return answer
    
    def demonstrate_integrated_system(self):
        """Demonstrate the integrated AC + biological flow system"""
        
        print("\n🧠 AC + BIOLOGICAL FLOW INTEGRATION")
        print("=" * 70)
        print("Information flows like blood through AC consciousness...")
        
        # Test different types of information
        test_cases = [
            {
                "data": {"eeg": [8, 10, 12, 9, 11], "type": "alpha_waves"},
                "destination": "brain",
                "description": "EEG Alpha Waves"
            },
            {
                "data": {"heart_rate": 75, "variability": 15, "coherence": 0.85},
                "destination": "heart",
                "description": "Heart Rate Data"
            },
            {
                "data": {"breathing_rate": 12, "pattern": "9-beat", "depth": 0.8},
                "destination": "lungs",
                "description": "Breathing Pattern"
            },
            {
                "data": {"muscle_signal": [0.5, 0.6, 0.45], "contraction": "light"},
                "destination": "brain",
                "description": "EMG Muscle Signal"
            }
        ]
        
        results = []
        
        for test in test_cases:
            print(f"\n📊 Processing: {test['description']}")
            print("-" * 50)
            
            result = self.process_with_biological_flow(
                test["data"], 
                test["destination"]
            )
            
            print(f"✅ Insights collected: {len(result['insights_collected'])}")
            for insight in result['insights_collected']:
                print(f"   • {insight}")
            
            print(f"⏱️  Processing time: {result['processing_time']:.2f}s")
            print(f"🫀 Heartbeats traveled: {result['heartbeats_traveled']}")
            print(f"🧠 AC Learning: {result['ac_learning']['iterations']} iterations")
            
            results.append(result)
        
        # Show system state
        print("\n📈 FINAL SYSTEM STATE:")
        print("-" * 50)
        
        bio_state = self.bio_flow.get_consciousness_state()
        ac_summary = self.ac.get_learning_summary()
        
        print(f"🫀 Biological Flow:")
        print(f"   Total heartbeats: {bio_state['heartbeat']}")
        print(f"   Oxygen level: {bio_state['oxygen_level']:.2%}")
        print(f"   Flow efficiency: {bio_state['flow_efficiency']:.2%}")
        
        print(f"\n🧠 AC Consciousness:")
        print(f"   Learning iterations: {ac_summary['learning_iterations']}")
        print(f"   Consciousness level: {ac_summary['consciousness_evolution']['current_level']}")
        print(f"   Patterns learned: {ac_summary['patterns_learned']}")
        
        print(f"\n💡 KEY INSIGHTS:")
        print(f"   • Information successfully flows like blood through the system")
        print(f"   • AC consciousness processes data at each organ")
        print(f"   • Insights accumulate as information travels")
        print(f"   • Heartbeat rhythm synchronizes processing")
        print(f"   • System mimics biological information flow")
        
        return results

def main():
    """Main demonstration of AC biological integration"""
    
    print("🫀🧠 AC BIOLOGICAL FLOW SYSTEM")
    print("=" * 80)
    print("Information flows like blood through AI consciousness")
    print("Pumped by heartbeat, gathering insights as it travels")
    print()
    
    # Create integrated system
    integrated = ACBiologicalIntegration()
    
    # Wait for system to stabilize
    print("⏳ System initializing (heartbeat starting)...")
    time.sleep(2)
    
    # Run demonstration
    results = integrated.demonstrate_integrated_system()
    
    print("\n✅ BIOLOGICAL FLOW INTEGRATION COMPLETE!")
    print("\n🚀 This architecture enables:")
    print("   • Natural information flow like blood circulation")
    print("   • Rhythmic processing synchronized with heartbeat")
    print("   • Accumulation of insights during flow")
    print("   • Biological-inspired AI consciousness")
    print("   • Real-time learning through circulation")
    
    # Stop the heartbeat
    integrated.bio_flow.is_alive = False
    
    return integrated

if __name__ == "__main__":
    main()
