#main
from will_system import WillSystem
from intellect_system import IntellectSystem
from understanding_system import UnderstandingSystem
from decision_system import DecisionSystem
from sensory_system import SensorySystem
from presentation_system import PresentationSystem
from thought_system import ThoughtSystem
from reason_system import ReasonSystem
from utils import log_message

def main():
    log_message("Starting VTAS Thought Constellation Simulation.")

    # Initialize all systems
    will_system = WillSystem()
    intellect_system = IntellectSystem()
    understanding_system = UnderstandingSystem()
    decision_system = DecisionSystem()
    sensory_system = SensorySystem()
    presentation_system = PresentationSystem()
    thought_system = ThoughtSystem()
    reason_system = ReasonSystem()

    # Register systems with the Thought System
    thought_system.register_system("WillSystem", will_system)
    thought_system.register_system("IntellectSystem", intellect_system)
    thought_system.register_system("UnderstandingSystem", understanding_system)
    thought_system.register_system("DecisionSystem", decision_system)
    thought_system.register_system("SensorySystem", sensory_system)
    thought_system.register_system("PresentationSystem", presentation_system)
    thought_system.register_system("ReasonSystem", reason_system)

    # Start the mission
    intention_message = will_system.define_intention()
    response = thought_system.route_message(intention_message)

    log_message(f"Final Response: {response}")
    log_message("Thought Constellation Simulation Completed.")

if __name__ == "__main__":
    main()