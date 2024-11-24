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
        if detected_class != self.last_class:
            # Reset count if a new class is detected
            self.last_class = detected_class
            self.last_class_count = 1
        else:
            self.last_class_count += 1

        if self.last_class_count == 10:
            print("Command", detected_class, self.detected_classes)
            if self.detected_classes and (timestamp - self.detected_classes[-1]['timestamp'] > 5):
                self.detected_classes.clear()

            if (not self.detected_classes) or self.detected_classes[-1]['class'] != detected_class:
                self.detected_classes.append({'class': detected_class, 'timestamp': timestamp})
                    
            self.process_command()

    def process_command(self):
        # Find the command sequence from the config.commands dictionary
        for command_name, command_sequence in COMMANDS.items():
            recent_classes = [entry['class'] for entry in self.detected_classes[-len(command_sequence):]]
            if recent_classes == command_sequence:
                self.execute_command(command_name)
                break

    def execute_command(self, command_name: str):
        # Function (3): Execute the command (right now just types the key)
        print("Executing command:", command_name)
        self.detected_classes.clear()
        pyautogui.press(command_name)