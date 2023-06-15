LETTERS = "ABCDEFGHIJKLAMNOPQRSTUVWXYZ"

CONFIG_FILE = "config"

def base_plugboard():
    return {l:l for l in LETTERS}

def read_configuration():
    with open(CONFIG_FILE, "r") as config_file:
        config = config_file.read().split(" ")
    rotors = config[:4]
    offsets = [int(x) for x in config[4:8]]
    plugboard = base_plugboard()
    for cable in config[8:-1]:
        l1, l2 = cable
        plugboard[l1] = l2
        plugboard[l2] = l1
    reflector = config[-1]
    return (rotors, offsets, plugboard, reflector)


