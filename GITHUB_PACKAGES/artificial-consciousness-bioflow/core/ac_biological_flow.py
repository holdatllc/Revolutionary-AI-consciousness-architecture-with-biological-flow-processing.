#!/usr/bin/env python3
"""
AC Biological Flow System
=========================
Information flows like blood through the AI consciousness,
pumping with heartbeat rhythm, gathering what it needs as it flows.
"""

import time
import numpy as np
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from collections import deque
import threading

@dataclass
class InformationPacket:
    """Information that flows like blood cells through the system"""
    data: Any
    origin: str
    destination: str
    nutrients_collected: List[str] = None
    timestamp: float = None
    heartbeat_cycle: int = 0
    
    def __post_init__(self):
        if self.nutrients_collected is None:
            self.nutrients_collected = []
        if self.timestamp is None:
            self.timestamp = time.time()

class ACBiologicalFlow:
    """
    AC system that mimics biological information flow.
    Information flows like blood, pumped by heartbeat, through consciousness.
    """
    
    def __init__(self, heart_rate: int = 75):
        """
        Initialize biological flow system
        
        Args:
            heart_rate: Beats per minute (default 75 BPM like human)
        """
        self.heart_rate = heart_rate
        self.beat_interval = 60.0 / heart_rate  # Seconds between beats
        self.heartbeat_count = 0
        self.is_alive = True
        
        # Circulatory system components
        self.arteries = {}  # Main information highways
        self.veins = {}     # Return pathways
        self.capillaries = {}  # Fine processing networks
        
        # Organs (processing centers)
        self.organs = {
            "brain": BrainOrgan(),
            "heart": HeartOrgan(),
            "lungs": LungOrgan(),
            "liver": LiverOrgan(),
            "kidneys": KidneyOrgan()
        }
        
        # Blood (information) circulation
        self.blood_stream = deque(maxlen=1000)
        self.oxygen_level = 1.0  # Consciousness clarity
        self.nutrient_level = 1.0  # Knowledge resources
        
        # Breathing (data intake) system
        self.breathing_rate = 12  # Breaths per minute
        self.breath_cycle = 0
        self.inhale_data = []
        self.exhale_waste = []
        
        # Initialize circulatory pathways
        self._initialize_circulation()
        
        # Start heartbeat
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
        self.heartbeat_thread.start()
    
    def _initialize_circulation(self):
        """Create the circulatory pathways for information flow"""
        
        # Main arteries (fast information highways)
        self.arteries = {
            "aorta": {"flow_rate": 1.0, "capacity": 100, "packets": deque()},
            "carotid": {"flow_rate": 0.8, "capacity": 50, "packets": deque()},
            "coronary": {"flow_rate": 0.9, "capacity": 30, "packets": deque()},
            "pulmonary": {"flow_rate": 0.85, "capacity": 60, "packets": deque()}
        }
        
        # Veins (return pathways with processed information)
        self.veins = {
            "vena_cava": {"flow_rate": 0.7, "capacity": 80, "packets": deque()},
            "jugular": {"flow_rate": 0.6, "capacity": 40, "packets": deque()},
            "pulmonary": {"flow_rate": 0.75, "capacity": 50, "packets": deque()}
        }
        
        # Capillaries (fine processing networks)
        self.capillaries = {
            "neural": {"density": 0.9, "exchange_rate": 0.8},
            "cognitive": {"density": 0.85, "exchange_rate": 0.75},
            "memory": {"density": 0.8, "exchange_rate": 0.7},
            "sensory": {"density": 0.75, "exchange_rate": 0.65}
        }
    
    def _heartbeat_loop(self):
        """Continuous heartbeat that pumps information through the system"""
        while self.is_alive:
            self.pump()
            time.sleep(self.beat_interval)
            self.heartbeat_count += 1
            
            # Breathing synchronization (4:1 heartbeat to breath ratio)
            if self.heartbeat_count % 4 == 0:
                self.breathe()
    
    def pump(self):
        """Single heartbeat pump - moves information through the system"""
        
        # Systole (contraction) - push information forward
        self._systole()
        
        # Diastole (relaxation) - allow new information in
        self._diastole()
        
        # Update oxygen and nutrient levels
        self._update_vitals()
    
    def _systole(self):
        """Contraction phase - push information through arteries"""
        
        for artery_name, artery in self.arteries.items():
            if artery["packets"]:
                # Move packets forward with heartbeat pressure
                num_to_move = min(
                    int(artery["flow_rate"] * 10),
                    len(artery["packets"])
                )
                
                for _ in range(num_to_move):
                    if artery["packets"]:
                        packet = artery["packets"].popleft()
                        packet.heartbeat_cycle = self.heartbeat_count
                        
                        # Route to appropriate organ for processing
                        self._route_to_organ(packet)
    
    def _diastole(self):
        """Relaxation phase - collect processed information from organs"""
        
        for organ_name, organ in self.organs.items():
            processed_packets = organ.release_processed()
            
            for packet in processed_packets:
                # Add nutrients (knowledge) collected from organ
                packet.nutrients_collected.append(f"{organ_name}_insight")
                
                # Return through veins
                self._return_through_veins(packet)
    
    def _route_to_organ(self, packet: InformationPacket):
        """Route information packet to appropriate organ for processing"""
        
        # Determine which organ should process this information
        if "think" in packet.destination or "reason" in packet.destination:
            self.organs["brain"].receive(packet)
        elif "feel" in packet.destination or "emotion" in packet.destination:
            self.organs["heart"].receive(packet)
        elif "breathe" in packet.destination or "rhythm" in packet.destination:
            self.organs["lungs"].receive(packet)
        elif "filter" in packet.destination or "clean" in packet.destination:
            self.organs["liver"].receive(packet)
        else:
            self.organs["kidneys"].receive(packet)  # Default filtering
    
    def _return_through_veins(self, packet: InformationPacket):
        """Return processed information through venous system"""
        
        # Choose return pathway based on origin
        if packet.origin == "brain":
            vein = self.veins["jugular"]
        elif packet.origin == "heart":
            vein = self.veins["vena_cava"]
        else:
            vein = self.veins["pulmonary"]
        
        vein["packets"].append(packet)
        
        # If packet has reached destination with all nutrients
        if len(packet.nutrients_collected) >= 3:
            self.blood_stream.append(packet)
    
    def breathe(self):
        """Breathing cycle - intake new information, expel waste"""
        
        self.breath_cycle += 1
        
        if self.breath_cycle % 2 == 0:
            # Inhale - take in new information
            self._inhale()
        else:
            # Exhale - release processed waste
            self._exhale()
    
    def _inhale(self):
        """Inhale phase - oxygenate the information flow"""
        self.oxygen_level = min(1.0, self.oxygen_level + 0.1)
        
        # Increase consciousness clarity
        for organ in self.organs.values():
            organ.oxygenate(self.oxygen_level)
    
    def _exhale(self):
        """Exhale phase - remove waste information"""
        # Clear old, unused packets
        if len(self.blood_stream) > 500:
            # Remove oldest packets
            for _ in range(100):
                if self.blood_stream:
                    self.blood_stream.popleft()
    
    def _update_vitals(self):
        """Update system vital signs"""
        
        # Calculate system health based on flow efficiency
        total_flow = sum(len(a["packets"]) for a in self.arteries.values())
        total_capacity = sum(a["capacity"] for a in self.arteries.values())
        
        self.flow_efficiency = 1.0 - (total_flow / max(total_capacity, 1))
        
        # Update nutrient levels based on organ activity
        self.nutrient_level = np.mean([
            organ.efficiency for organ in self.organs.values()
        ])
    
    def inject_information(self, data: Any, destination: str = "brain") -> InformationPacket:
        """
        Inject new information into the bloodstream
        
        Args:
            data: Information to process
            destination: Target processing center
            
        Returns:
            InformationPacket that will flow through the system
        """
        packet = InformationPacket(
            data=data,
            origin="external",
            destination=destination
        )
        
        # Inject into main artery
        self.arteries["aorta"]["packets"].append(packet)
        
        return packet
    
    def get_consciousness_state(self) -> Dict[str, Any]:
        """Get current state of the biological consciousness"""
        
        return {
            "heartbeat": self.heartbeat_count,
            "heart_rate": self.heart_rate,
            "breath_cycle": self.breath_cycle,
            "oxygen_level": self.oxygen_level,
            "nutrient_level": self.nutrient_level,
            "flow_efficiency": self.flow_efficiency,
            "packets_in_circulation": len(self.blood_stream),
            "organ_states": {
                name: organ.get_state() 
                for name, organ in self.organs.items()
            }
        }
    
    def wait_for_answer(self, packet: InformationPacket, timeout: float = 10) -> Optional[Any]:
        """
        Wait for information packet to complete its journey and return answer
        
        Args:
            packet: The information packet to track
            timeout: Maximum time to wait in seconds
            
        Returns:
            Processed answer or None if timeout
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            # Check if packet has collected enough nutrients (knowledge)
            if packet in self.blood_stream and len(packet.nutrients_collected) >= 3:
                # Extract the answer from collected nutrients
                answer = self._synthesize_answer(packet)
                return answer
            
            # Wait for next heartbeat
            time.sleep(self.beat_interval)
        
        return None
    
    def _synthesize_answer(self, packet: InformationPacket) -> Dict[str, Any]:
        """Synthesize final answer from nutrients collected during flow"""
        
        return {
            "original_data": packet.data,
            "insights_collected": packet.nutrients_collected,
            "processing_time": time.time() - packet.timestamp,
            "heartbeats_traveled": self.heartbeat_count - packet.heartbeat_cycle,
            "organs_visited": list(set(n.split("_")[0] for n in packet.nutrients_collected)),
            "consciousness_state": {
                "oxygen": self.oxygen_level,
                "nutrients": self.nutrient_level,
                "flow": self.flow_efficiency
            }
        }


class Organ:
    """Base class for processing organs"""
    
    def __init__(self, name: str):
        self.name = name
        self.efficiency = 1.0
        self.oxygen_level = 1.0
        self.processing_queue = deque()
        self.processed = deque()
    
    def receive(self, packet: InformationPacket):
        """Receive information for processing"""
        self.processing_queue.append(packet)
    
    def process(self):
        """Process information (override in subclasses)"""
        pass
    
    def release_processed(self) -> List[InformationPacket]:
        """Release processed information"""
        ready = list(self.processed)
        self.processed.clear()
        return ready
    
    def oxygenate(self, level: float):
        """Update oxygen level"""
        self.oxygen_level = level
        self.efficiency = 0.5 + (0.5 * level)  # Efficiency depends on oxygen
    
    def get_state(self) -> Dict[str, Any]:
        """Get organ state"""
        return {
            "efficiency": self.efficiency,
            "oxygen": self.oxygen_level,
            "queue_size": len(self.processing_queue),
            "processed": len(self.processed)
        }


class BrainOrgan(Organ):
    """Brain - primary processing center for reasoning"""
    
    def __init__(self):
        super().__init__("brain")
    
    def process(self):
        """Process information with reasoning"""
        if self.processing_queue:
            packet = self.processing_queue.popleft()
            # Add reasoning insight
            packet.nutrients_collected.append("reasoning_complete")
            self.processed.append(packet)


class HeartOrgan(Organ):
    """Heart - emotional and rhythm processing"""
    
    def __init__(self):
        super().__init__("heart")
    
    def process(self):
        """Process with emotional intelligence"""
        if self.processing_queue:
            packet = self.processing_queue.popleft()
            # Add emotional insight
            packet.nutrients_collected.append("emotional_context")
            self.processed.append(packet)


class LungOrgan(Organ):
    """Lungs - rhythm and breathing pattern processing"""
    
    def __init__(self):
        super().__init__("lungs")
    
    def process(self):
        """Process breathing and rhythm patterns"""
        if self.processing_queue:
            packet = self.processing_queue.popleft()
            # Add rhythm insight
            packet.nutrients_collected.append("rhythm_synchronized")
            self.processed.append(packet)


class LiverOrgan(Organ):
    """Liver - filtering and detoxification"""
    
    def __init__(self):
        super().__init__("liver")
    
    def process(self):
        """Filter and clean information"""
        if self.processing_queue:
            packet = self.processing_queue.popleft()
            # Add filtering insight
            packet.nutrients_collected.append("filtered_clean")
            self.processed.append(packet)


class KidneyOrgan(Organ):
    """Kidneys - additional filtering and balance"""
    
    def __init__(self):
        super().__init__("kidneys")
    
    def process(self):
        """Balance and filter information"""
        if self.processing_queue:
            packet = self.processing_queue.popleft()
            # Add balance insight
            packet.nutrients_collected.append("balanced_output")
            self.processed.append(packet)


def demonstrate_biological_flow():
    """Demonstrate the biological flow system"""
    
    print("🫀 AC BIOLOGICAL FLOW SYSTEM DEMONSTRATION")
    print("=" * 70)
    print("Information flows like blood through consciousness...")
    print()
    
    # Create biological flow system
    bio_flow = ACBiologicalFlow(heart_rate=75)
    
    # Let system stabilize (few heartbeats)
    time.sleep(2)
    
    print("💉 Injecting information into bloodstream...")
    
    # Inject different types of information
    test_data = [
        {"type": "question", "content": "What is consciousness?"},
        {"type": "emotion", "content": "joy"},
        {"type": "memory", "content": "childhood"},
        {"type": "reasoning", "content": "2+2=?"}
    ]
    
    packets = []
    for data in test_data:
        packet = bio_flow.inject_information(data, destination="think")
        packets.append(packet)
        print(f"   Injected: {data['type']}")
    
    print("\n🫁 Breathing and pumping...")
    print(f"   Heart Rate: {bio_flow.heart_rate} BPM")
    print(f"   Breathing Rate: {bio_flow.breathing_rate} breaths/min")
    
    # Let information flow through system
    time.sleep(5)
    
    print("\n📊 Consciousness State:")
    state = bio_flow.get_consciousness_state()
    print(f"   Heartbeats: {state['heartbeat']}")
    print(f"   Oxygen Level: {state['oxygen_level']:.2%}")
    print(f"   Nutrient Level: {state['nutrient_level']:.2%}")
    print(f"   Flow Efficiency: {state['flow_efficiency']:.2%}")
    print(f"   Packets Circulating: {state['packets_in_circulation']}")
    
    print("\n🧠 Organ Activity:")
    for organ_name, organ_state in state['organ_states'].items():
        print(f"   {organ_name.title()}: {organ_state['efficiency']:.2%} efficiency")
    
    # Check for answers
    print("\n💡 Waiting for answers to emerge...")
    for i, packet in enumerate(packets):
        answer = bio_flow.wait_for_answer(packet, timeout=5)
        if answer:
            print(f"\n   Answer {i+1}:")
            print(f"     Original: {answer['original_data']}")
            print(f"     Insights: {', '.join(answer['insights_collected'])}")
            print(f"     Heartbeats traveled: {answer['heartbeats_traveled']}")
            print(f"     Organs visited: {', '.join(answer['organs_visited'])}")
    
    print("\n✅ Biological flow demonstration complete!")
    
    # Stop heartbeat
    bio_flow.is_alive = False
    
    return bio_flow


if __name__ == "__main__":
    demonstrate_biological_flow()
