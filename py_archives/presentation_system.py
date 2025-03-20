from utils import log_message, validate_message
from typing import Dict, Any

class PresentationSystem:
    def __init__(self):
        self.reports = []

    def communicate(self, action: str, parameters: Dict[str, str]) -> None:
        """Communicates the action externally."""
        report = f"Action: {action}, Details: {parameters}"
        self.reports.append(report)
        log_message(f"Presentation System: Communicating - {report}")

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "PresentationSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "ACTION_REQUEST":
            self.communicate(message["attributes"]["action"], message["attributes"]["parameters"])
            return {
                "message_type": "STATUS_UPDATE",
                "source": "PresentationSystem",
                "target": message["source"],
                "attributes": {"status": "completed", "details": "Action communicated"}
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "PresentationSystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported message"}
        }