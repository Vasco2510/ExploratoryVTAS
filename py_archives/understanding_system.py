from utils import SpeciesObservation, log_message, validate_message
from typing import Dict, Any, Optional

class UnderstandingSystem:
    def __init__(self):
        self.context: Dict[str, SpeciesObservation] = {}

    def contextualize_observation(self, observation: SpeciesObservation) -> Dict[str, str]:
        """Contextualizes an observation."""
        context = {
            "habitat_match": "yes" if observation.natural_habitat == "Peruvian jungle" else "no",
            "behavioral_insight": f"Active during {observation.behavioral_patterns['activity']}"
        }
        return context

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "UnderstandingSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "PROVIDE_DATA":
            observation = message["attributes"]["data"]
            context = self.contextualize_observation(observation)
            self.context[str(id(observation))] = observation
            return {
                "message_type": "REPORT_OBSERVATION",
                "source": "UnderstandingSystem",
                "target": "ThoughtSystem",
                "attributes": {"observation": context, "confidence": observation.confidence}
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "UnderstandingSystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported message"}
        }