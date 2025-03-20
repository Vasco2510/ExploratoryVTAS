# decision_system.py
from utils import log_message, validate_message
from typing import Dict, Any

class DecisionSystem:
    def __init__(self):
        self.actions = []

    def select_action(self, observation: Dict[str, str], confidence: float) -> str:
        """Selects an action based on the observation."""
        if confidence > 0.5:
            action = "Record species data"
        else:
            action = "Continue exploration"
        self.actions.append(action)
        return action

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "DecisionSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "REPORT_OBSERVATION":
            observation = message["attributes"]["observation"]
            confidence = message["attributes"]["confidence"]
            action = self.select_action(observation, confidence)
            return {
                "message_type": "ACTION_REQUEST",
                "source": "DecisionSystem",
                "target": "PresentationSystem",
                "attributes": {"action": action, "parameters": {"details": observation}}
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "DecisionSystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported message"}
        }