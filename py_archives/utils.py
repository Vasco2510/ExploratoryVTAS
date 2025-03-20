# utils.py
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
import random
from datetime import datetime

# Communication Language Dictionary
MESSAGE_TYPES = {
    "REQUEST_DATA": ["source", "target", "data_type"],
    "PROVIDE_DATA": ["source", "target", "data"],
    "REPORT_OBSERVATION": ["source", "observation", "confidence"],
    "ACTION_REQUEST": ["source", "target", "action", "parameters"],
    "STATUS_UPDATE": ["source", "status", "details"],
    "VALIDATION_REQUEST": ["source", "target", "hypothesis", "context"],
    "VALIDATION_RESPONSE": ["source", "target", "result", "reason"]
}

@dataclass
class SensorData:
    """Represents raw sensor data."""
    image: str
    temperature: float
    humidity: float
    motion: bool

@dataclass
class SpeciesObservation:
    """Represents an observation of a potential species."""
    physical_characteristics: Dict[str, str]
    natural_habitat: str
    behavioral_patterns: Dict[str, str]
    confidence: float = 0.0

# Simulated species database
KNOWN_SPECIES = {
    "Andean Condor": {
        "physical_characteristics": {"size": "large", "color": "black", "patterns": "white collar"},
        "natural_habitat": "Andean mountains",
        "behavioral_patterns": {"feeding": "carrion", "migration": "seasonal", "activity": "diurnal"}
    },
    "Jaguar": {
        "physical_characteristics": {"size": "medium", "color": "yellow", "patterns": "spotted"},
        "natural_habitat": "Peruvian jungle",
        "behavioral_patterns": {"feeding": "carnivore", "migration": "none", "activity": "nocturnal"}
    }
}

def simulate_sensor_reading() -> SensorData:
    """Simulates sensor data for testing."""
    return SensorData(
        image=random.choice(["yellow spotted animal", "large black bird with white collar", "unknown"]),
        temperature=random.uniform(20.0, 35.0),
        humidity=random.uniform(50.0, 90.0),
        motion=random.choice([True, False])
    )

def log_message(message: str) -> None:
    """Logs a message with a timestamp."""
    print(f"[{datetime.now()}] {message}")

def validate_message(message: Dict[str, Any]) -> bool:
    """Validates a message against the communication language grammar."""
    if not all(key in message for key in ["message_type", "source", "target", "attributes"]):
        return False
    message_type = message["message_type"]
    if message_type not in MESSAGE_TYPES:
        return False
    required_attrs = MESSAGE_TYPES[message_type]
    return all(attr in message["attributes"] for attr in required_attrs)