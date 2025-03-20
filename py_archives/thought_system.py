# thought_system.py
from utils import log_message, validate_message
from typing import Dict, Any

class ThoughtSystem:
    def __init__(self):
        self.systems = {}

    def register_system(self, system_name: str, system: Any) -> None:
        """Registers a system for communication."""
        self.systems[system_name] = system

    def route_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Routes messages between systems."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "ThoughtSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        target = message["target"]
        if target == "ThoughtSystem":
            if message["message_type"] == "ACTION_REQUEST" and message["attributes"]["action"] == "start_mission":
                log_message("Thought System: Starting mission.")
                return {
                    "message_type": "ACTION_REQUEST",
                    "source": "ThoughtSystem",
                    "target": "SensorySystem",
                    "attributes": {"action": "capture_data", "parameters": {}}
                }
            elif message["message_type"] == "REPORT_OBSERVATION":
                return {
                    "message_type": "REPORT_OBSERVATION",
                    "source": "ThoughtSystem",
                    "target": "DecisionSystem",
                    "attributes": message["attributes"]
                }
        if target in self.systems:
            response = self.systems[target].process_message(message)
            if response["message_type"] != "STATUS_UPDATE" or response["attributes"]["status"] != "error":
                return self.route_message(response)
        return {
            "message_type": "STATUS_UPDATE",
            "source": "ThoughtSystem",
            "target": message["source"],
            "attributes": {"status": "completed", "details": "Message processed"}
        }