import time
import config
import pyautogui

from config import COMMANDS

# Example usage
# parser = CommandParser()
# parser.store_class(1, time.time())
# parser.store_class(2, time.time())
# parser.store_class(3, time.time())

class CommandParser:
    def __init__(self):
        self.detected_classes = []
        self.last_class = None
        self.last_class_count = 0

    def store_class(self, detected_class: int, timestamp: float):
        # Function (1): Store a detected class and execute process_command()
        if 0 <= detected_class <= 10:
            if detected_class != self.last_class:
                # Reset count if a new class is detected
                self.last_class = detected_class
                self.last_class_count = 1
            else:
                # Increment count for repeated classes
                self.last_class_count += 1

            if self.last_class_count >= 10:
                if not self.detected_classes or (timestamp - self.detected_classes[-1]['timestamp'] <= 1.2):
                    # Add the detected class if it is different and within 1.2 seconds of the last non-zero class
                    if not self.detected_classes or self.detected_classes[-1]['class'] != detected_class:
                        self.detected_classes.append({'class': detected_class, 'timestamp': timestamp})
                    self.process_command()

    def process_command(self):
        # Function (2): Process the detected classes and execute the command
        # Create a copy and filter out rest state classes (0)
        filtered_classes = [entry['class'] for entry in self.detected_classes if entry['class'] != 0]

        # Find the command sequence from the config.commands dictionary
        for command_name, command_sequence in COMMANDS.items():
            if filtered_classes == command_sequence:
                self.execute_command(command_name)
                break

        # Clear the detected classes after processing
        self.detected_classes.clear()

    def execute_command(self, command_name: str):
        # Function (3): Execute the command (right now just types the key)
        pyautogui.press(command_name)