# will_system.py
from utils import log_message, validate_message
from typing import Dict, Any

class WillSystem:
    def __init__(self):
        self.mission = "Explore and identify new animal species in the Peruvian jungle."
        self.energy_level = 100.0

    def define_intention(self) -> Dict[str, Any]:
        """Defines the intention to drive the mission."""
        message = {
            "message_type": "ACTION_REQUEST",
            "source": "WillSystem",
            "target": "ThoughtSystem",
            "attributes": {
                "action": "start_mission",
                "parameters": {"mission": self.mission}
            }
        }
        log_message(f"Will System: Sending intention - {message}")
        return message

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "WillSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "STATUS_UPDATE" and message["attributes"]["status"] == "low_energy":
            self.energy_level = 10.0
            log_message("Will System: Received low energy warning. Adjusting operations.")
        return {
            "message_type": "STATUS_UPDATE",
            "source": "WillSystem",
            "target": message["source"],
            "attributes": {"status": "received", "details": "Message processed"}
        }