from utils import SensorData, simulate_sensor_reading, log_message, validate_message
from typing import Dict, Any

class SensorySystem:
    def __init__(self):
        self.battery_level = 80.0

    def capture_data(self) -> SensorData:
        """Captures environmental data."""
        return simulate_sensor_reading()

    def check_health(self) -> bool:
        """Checks system health."""
        if self.battery_level < 20.0:
            return False
        return True

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Processes incoming messages."""
        if not validate_message(message):
            return {
                "message_type": "STATUS_UPDATE",
                "source": "SensorySystem",
                "target": message["source"],
                "attributes": {"status": "error", "details": "Invalid message format"}
            }
        if message["message_type"] == "ACTION_REQUEST" and message["attributes"]["action"] == "capture_data":
            if not self.check_health():
                return {
                    "message_type": "STATUS_UPDATE",
                    "source": "SensorySystem",
                    "target": "WillSystem",
                    "attributes": {"status": "low_energy", "details": "Battery level critical"}
                }
            sensor_data = self.capture_data()
            return {
                "message_type": "REQUEST_DATA",
                "source": "SensorySystem",
                "target": "IntellectSystem",
                "attributes": {"data_type": "sensor_data", "data": sensor_data}
            }
        return {
            "message_type": "STATUS_UPDATE",
            "source": "SensorySystem",
            "target": message["source"],
            "attributes": {"status": "error", "details": "Unsupported action"}
        }