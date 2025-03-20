# intellect_system.py
from utils import KNOWN_SPECIES, SensorData, SpeciesObservation, log_message, validate_message
from typing import Dict, Any, Optional

class IntellectSystem:
    def __init__(self):
        self.species_database = KNOWN_SPECIES
        self.observations: Dict[str, SpeciesObservation] = {}

    def analyze_data(self, sensor_data: SensorData) -> SpeciesObservation:
        """Analyzes sensor data to create an observation."""
        observation = SpeciesObservation(
            physical_characteristics={"color": "unknown", "patterns": "unknown"},
            natural_habitat="Peruvian jungle",
            behavioral_patterns={"activity": "unknown"}
        )
        if "yellow spotted" in sensor_data.image:
            observation.physical_characteristics = {"color": "yellow", "patterns": "spotted"}
            observation.behavioral_patterns["activity"] = "nocturnal"
        elif "large black bird" in sensor_data.image:
            observation.physical_characteristics = {"color": "black", "patterns": "white collar"}
            observation.behavioral_patterns["activity"] = "diurnal"
        return observation

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "IntellectSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "REQUEST_DATA" and message["attributes"]["data_type"] == "sensor_data":
            sensor_data = message["attributes"].get("data")
            observation = self.analyze_data(sensor_data)
            self.observations[str(id(observation))] = observation
            return {
                "message_type": "PROVIDE_DATA",
                "source": "IntellectSystem",
                "target": message["source"],
                "attributes": {"data": observation}
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "IntellectSystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported request"}
        }