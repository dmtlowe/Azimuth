MYO_ADDRESS = "DD:31:D8:40:BC:22"

DATA_INPUT_PATH = "data"

MODEL_PATH = "models/model.h5"
METADATA_PATH = "models/metadata.pkl"

# CLASSES = {
#     0: "rest", #saftey
#     1: "closed_fist", #go up
#     2: "ok", #go forwards
#     3: "f1", #finger 1
#     4: "f2", # finger 2
#     5: "f23", # finger 2+3
#     6: "f3", # finger 3
#     7: "f5", #finger 5
# }

CLASSES = {
    0: "rest", #saftey
    1: "first_finger", #go up
    2: "second_finger", #go down
    3: "third_finger", #go forwards
    # 4: "pointer_finger", #go backwards
    # 5: "peace", #roatate left
    # 6: "shaaa", #rotate right
    # 7: "peace_among_worlds", #do a flip
}

COMMANDS = {
    'h': [1, 1],
    'e': [1, 2],
    'l': [1, 3],
    'o': [2, 1],
    'space': [2, 2],
    'w': [2, 3],
    'r': [3, 1],
    'd': [3, 2],
    'backspace': [3, 3]
}

