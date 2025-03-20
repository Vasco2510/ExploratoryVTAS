# reason_system.py
from utils import log_message, validate_message
from typing import Dict, Any

class ReasonSystem:
    def validate_hypothesis(self, hypothesis: Dict[str, str], context: Dict[str, str]) -> Dict[str, str]:
        """Validates a hypothesis."""
        if context["habitat_match"] == "yes":
            return {"result": "valid", "reason": "Observation matches expected habitat"}
        return {"result": "invalid", "reason": "Observation does not match expected habitat"}

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "ReasonSystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "VALIDATION_REQUEST":
            hypothesis = message["attributes"]["hypothesis"]
            context = message["attributes"]["context"]
            validation = self.validate_hypothesis(hypothesis, context)
            return {
                "message_type": "VALIDATION_RESPONSE",
                "source": "ReasonSystem",
                "target": message["source"],
                "attributes": validation
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "ReasonSystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported message"}
        }