MYO_ADDRESS = "DD:31:D8:40:BC:22"

DATA_INPUT_PATH = "data"

MODEL_PATH = "models/model.h5"
METADATA_PATH = "models/metadata.pkl"

CLASSES = {
    0: "rest", #saftey
    1: "closed_fist", #go up
    2: "ok", #go forwards
    3: "f1", #finger 1
    4: "f2", # finger 2
    5: "f23", # finger 2+3
    6: "f3", # finger 3
    7: "f5", #finger 5
}

COMMANDS = {
    'h': [3, 3],
    'e': [3, 4],
    'l': [3, 5],
    'o': [3, 6],
    'space': [3, 7],
    'w': [4, 4],
    'r': [4, 5],
    'd': [4, 6],
    'backspace': [4, 7]
}

