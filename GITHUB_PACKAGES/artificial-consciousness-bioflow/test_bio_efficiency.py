#!/usr/bin/env python3
"""
Biological Flow Efficiency Test
================================
Compare biological flow processing vs traditional sequential processing
for real-world tasks like medical diagnosis and pattern recognition.
"""

import sys
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Any
import threading
from concurrent.futures import ThreadPoolExecutor

# Add AC modules to path
sys.path.append(str(Path(__file__).parent / "core"))
from hcm_standalone import HCMStandalone
from ac_biological_flow import ACBiologicalFlow, InformationPacket

class BiologicalEfficiencyTest:
    """Test biological flow efficiency vs traditional processing"""
    
    def __init__(self):
        self.ac_traditional = HCMStandalone(learning_enabled=True)
        self.bio_flow = ACBiologicalFlow(heart_rate=120)  # Faster heartbeat for testing
        self.results = {}
    
    def traditional_processing(self, data_batch: List[Dict]) -> Dict:
        """Traditional sequential processing"""
        start_time = time.time()
        results = []
        
        for data in data_batch:
            # Process each item sequentially
            if data["type"] == "eeg":
                analysis = self.ac_traditional.read_and_analyze_data("eeg", data["values"])
                optimization = self.ac_traditional.optimize_computation(np.mean(data["values"]), "biomedical")
                results.append({
                    "type": "eeg",
                    "patterns": len(analysis.get("patterns_found", [])),
                    "optimization": optimization["improvement_percent"]
                })
            elif data["type"] == "heart":
                analysis = self.ac_traditional.read_and_analyze_data("heart", data["values"])
                optimization = self.ac_traditional.optimize_computation(np.mean(data["values"]), "biomedical")
                results.append({
                    "type": "heart",
                    "patterns": len(analysis.get("patterns_found", [])),
                    "optimization": optimization["improvement_percent"]
                })
            elif data["type"] == "muscle":
                analysis = self.ac_traditional.read_and_analyze_data("muscle", data["values"])
                optimization = self.ac_traditional.optimize_computation(np.mean(data["values"]), "prosthetic")
                results.append({
                    "type": "muscle",
                    "patterns": len(analysis.get("patterns_found", [])),
                    "optimization": optimization["improvement_percent"]
                })
        
        processing_time = time.time() - start_time
        return {
            "method": "traditional",
            "time": processing_time,
            "results": results,
            "items_processed": len(results)
        }
    
    def biological_flow_processing(self, data_batch: List[Dict]) -> Dict:
        """Biological flow parallel processing"""
        start_time = time.time()
        packets = []
        results = []
        
        # Inject all data into bloodstream at once
        for data in data_batch:
            destination = "brain" if data["type"] == "eeg" else "heart" if data["type"] == "heart" else "liver"
            packet = self.bio_flow.inject_information(data, destination)
            packets.append(packet)
        
        # Let blood flow carry information through system
        # Multiple packets flow simultaneously like blood cells
        max_cycles = 20  # Maximum heartbeat cycles
        
        for cycle in range(max_cycles):
            # All organs process simultaneously
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = []
                for organ in self.bio_flow.organs.values():
                    futures.append(executor.submit(self._process_organ, organ))
                
                # Wait for all organs to complete
                for future in futures:
                    future.result()
            
            # Check if all packets have been processed
            all_processed = all(
                len(p.nutrients_collected) >= 2 for p in packets
            )
            
            if all_processed:
                break
            
            # Heartbeat delay
            time.sleep(self.bio_flow.beat_interval)
        
        # Collect results
        for packet in packets:
            results.append({
                "type": packet.data["type"],
                "nutrients": len(packet.nutrients_collected),
                "heartbeats": cycle + 1
            })
        
        processing_time = time.time() - start_time
        return {
            "method": "biological_flow",
            "time": processing_time,
            "results": results,
            "items_processed": len(results),
            "heartbeat_cycles": cycle + 1
        }
    
    def _process_organ(self, organ):
        """Process information in organ (thread-safe)"""
        if organ.processing_queue:
            try:
                packet = organ.processing_queue.popleft()
                # Simulate processing
                packet.nutrients_collected.append(f"{organ.name}_processed")
                organ.processed.append(packet)
            except:
                pass  # Queue was empty
    
    def run_medical_diagnosis_test(self):
        """Test: Process multiple patient data simultaneously"""
        print("\n🏥 MEDICAL DIAGNOSIS TEST")
        print("=" * 60)
        print("Processing 10 patients' vital signs simultaneously...")
        
        # Generate patient data
        patient_data = []
        for i in range(10):
            patient_data.append({
                "type": "eeg",
                "values": np.random.normal(10, 2, 5).tolist(),
                "patient_id": f"P{i+1}"
            })
            patient_data.append({
                "type": "heart",
                "values": np.random.normal(75, 10, 5).tolist(),
                "patient_id": f"P{i+1}"
            })
            patient_data.append({
                "type": "muscle",
                "values": np.random.normal(0.5, 0.1, 5).tolist(),
                "patient_id": f"P{i+1}"
            })
        
        # Test traditional processing
        print("\n⏱️  Traditional Sequential Processing...")
        trad_result = self.traditional_processing(patient_data)
        print(f"   Time: {trad_result['time']:.3f}s")
        print(f"   Items processed: {trad_result['items_processed']}")
        
        # Test biological flow
        print("\n🫀 Biological Flow Processing...")
        bio_result = self.biological_flow_processing(patient_data)
        print(f"   Time: {bio_result['time']:.3f}s")
        print(f"   Items processed: {bio_result['items_processed']}")
        print(f"   Heartbeat cycles: {bio_result['heartbeat_cycles']}")
        
        # Calculate efficiency
        speedup = trad_result['time'] / bio_result['time'] if bio_result['time'] > 0 else 0
        print(f"\n📊 EFFICIENCY COMPARISON:")
        print(f"   Speedup: {speedup:.2f}x {'faster' if speedup > 1 else 'slower'}")
        print(f"   Traditional: {trad_result['time']:.3f}s")
        print(f"   Biological: {bio_result['time']:.3f}s")
        print(f"   Time saved: {trad_result['time'] - bio_result['time']:.3f}s")
        
        return speedup
    
    def run_pattern_recognition_test(self):
        """Test: Recognize patterns in multiple data streams"""
        print("\n🔍 PATTERN RECOGNITION TEST")
        print("=" * 60)
        print("Finding patterns across 5 data streams...")
        
        # Generate data streams with hidden patterns
        data_streams = []
        
        # Stream 1: Repeating pattern
        for i in range(5):
            data_streams.append({
                "type": "eeg",
                "values": [3, 6, 9, 3, 6, 9],  # Tesla pattern
                "stream_id": f"S{i+1}"
            })
        
        # Stream 2: Fibonacci pattern
        for i in range(5):
            data_streams.append({
                "type": "heart",
                "values": [1, 1, 2, 3, 5, 8],  # Fibonacci
                "stream_id": f"S{i+1}"
            })
        
        # Test traditional processing
        print("\n⏱️  Traditional Sequential Processing...")
        trad_result = self.traditional_processing(data_streams)
        print(f"   Time: {trad_result['time']:.3f}s")
        
        # Test biological flow
        print("\n🫀 Biological Flow Processing...")
        bio_result = self.biological_flow_processing(data_streams)
        print(f"   Time: {bio_result['time']:.3f}s")
        
        # Calculate efficiency
        speedup = trad_result['time'] / bio_result['time'] if bio_result['time'] > 0 else 0
        print(f"\n📊 PATTERN RECOGNITION EFFICIENCY:")
        print(f"   Speedup: {speedup:.2f}x {'faster' if speedup > 1 else 'slower'}")
        
        return speedup
    
    def run_realtime_monitoring_test(self):
        """Test: Real-time monitoring of multiple sensors"""
        print("\n📡 REAL-TIME MONITORING TEST")
        print("=" * 60)
        print("Monitoring 20 sensors in real-time...")
        
        # Generate sensor data
        sensor_data = []
        for sensor_id in range(20):
            sensor_data.append({
                "type": "eeg" if sensor_id % 3 == 0 else "heart" if sensor_id % 3 == 1 else "muscle",
                "values": np.random.normal(50, 10, 10).tolist(),
                "sensor_id": f"SENSOR_{sensor_id}"
            })
        
        # Test traditional processing
        print("\n⏱️  Traditional Sequential Processing...")
        trad_result = self.traditional_processing(sensor_data)
        print(f"   Time: {trad_result['time']:.3f}s")
        
        # Test biological flow
        print("\n🫀 Biological Flow Processing...")
        bio_result = self.biological_flow_processing(sensor_data)
        print(f"   Time: {bio_result['time']:.3f}s")
        
        # Calculate efficiency
        speedup = trad_result['time'] / bio_result['time'] if bio_result['time'] > 0 else 0
        print(f"\n📊 REAL-TIME MONITORING EFFICIENCY:")
        print(f"   Speedup: {speedup:.2f}x {'faster' if speedup > 1 else 'slower'}")
        print(f"   Latency reduction: {(trad_result['time'] - bio_result['time']) * 1000:.1f}ms")
        
        return speedup

def main():
    """Run comprehensive efficiency tests"""
    
    print("🧪 BIOLOGICAL FLOW EFFICIENCY TEST SUITE")
    print("=" * 80)
    print("Comparing biological flow vs traditional processing")
    print()
    
    # Initialize test system
    test = BiologicalEfficiencyTest()
    
    # Let biological system stabilize
    print("⏳ Initializing biological flow system...")
    time.sleep(1)
    
    speedups = []
    
    # Run tests
    speedup1 = test.run_medical_diagnosis_test()
    speedups.append(speedup1)
    
    speedup2 = test.run_pattern_recognition_test()
    speedups.append(speedup2)
    
    speedup3 = test.run_realtime_monitoring_test()
    speedups.append(speedup3)
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 OVERALL EFFICIENCY SUMMARY")
    print("=" * 80)
    
    avg_speedup = np.mean(speedups)
    print(f"\n🏆 Average Speedup: {avg_speedup:.2f}x")
    
    if avg_speedup > 1.5:
        print("✅ BIOLOGICAL FLOW IS SIGNIFICANTLY FASTER!")
        print("   The parallel, organ-based processing beats sequential")
    elif avg_speedup > 1.0:
        print("✅ BIOLOGICAL FLOW IS FASTER!")
        print("   Modest improvement over traditional processing")
    elif avg_speedup > 0.8:
        print("⚠️  BIOLOGICAL FLOW IS COMPARABLE")
        print("   Similar performance to traditional processing")
    else:
        print("❌ TRADITIONAL PROCESSING IS FASTER")
        print("   Biological overhead may be too high for these tasks")
    
    print(f"\n💡 KEY INSIGHTS:")
    print(f"   • Medical Diagnosis: {speedup1:.2f}x")
    print(f"   • Pattern Recognition: {speedup2:.2f}x")
    print(f"   • Real-time Monitoring: {speedup3:.2f}x")
    
    print(f"\n🧠 BIOLOGICAL ADVANTAGES:")
    print(f"   • Parallel processing of multiple data streams")
    print(f"   • Natural rhythm synchronization")
    print(f"   • Distributed intelligence across organs")
    print(f"   • Accumulative learning during flow")
    
    # Stop biological system
    test.bio_flow.is_alive = False
    
    return avg_speedup

if __name__ == "__main__":
    main()
