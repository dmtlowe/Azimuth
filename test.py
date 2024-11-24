from command_parser import CommandParser
import time

command_parser = CommandParser()
for i in range(10):
    command_parser.store_class(1, time.time())

for i in range(10):
    command_parser.store_class(0, time.time())
    
for i in range(10):
    command_parser.store_class(1, time.time())
