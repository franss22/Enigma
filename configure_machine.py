import sys
from utils import *


available_rotors = ["I", "II", "III", "V", "VI", "VII", "VIII", "Beta"]
available_reflectors = ["UKB-c", "UKB-b"]

def save_configuration(args:list[str]):
    with open(CONFIG_FILE, "w") as config:
        config.write(" ".join(args))

if len(sys.argv) < 9:
    print("Wrong amount of arguments")
    sys.exit(1)

#Rotor configuration
rotors = sys.argv[1:5]
for i, rotor_arg in enumerate(rotors):
    if rotor_arg not in available_rotors:
        print(f"Rotor argument \"{rotor_arg}\" is not a valid rotor.")
        sys.exit(1)
    if rotor_arg == "Beta" and i in [0, 1, 2]:
        print(f"Rotor argument \"{rotor_arg}\" must cannot be in position {i}")
        sys.exit(1)

#Rotor position configuration
offsets = []
for offset_arg in sys.argv[5:9]:
    try:
        off = int(offset_arg)
        if off >=1 and off <=26:
            offsets.append(off)
        else:
            print(f"{off} is not a valid rotor position.")
            sys.exit(1)
    except ValueError as e:
        print(f"Offset value \"{offset_arg}\" is not a valid number.")
        sys.exit(1)

#Reflector configuration        
reflector = sys.argv[-1]
if reflector not in available_reflectors:
    print(f"Reflector argument \"{reflector}\" is not a valid reflector.")
    sys.exit(1)

#Plugboard Configuration
plugboard_args = sys.argv[9:-1] if len(sys.argv)>9 else []
used_letters = "".join(plugboard_args)
for cable in plugboard_args:
    if len(cable) != 2:
        print(f"{cable} is not a valid plugboard cable")
        sys.exit(1)
    l1, l2 = cable
    if l1 not in LETTERS or l2 not in LETTERS:
        print(f"{cable} is not a valid plugboard cable")
        sys.exit(1)
    if used_letters.count(l1)>1:
        print(F"Cannot plug 2 cables into letter \'{l1}\'")
        sys.exit(1)
    if used_letters.count(l2)>1:
        print(F"Cannot plug 2 cables into letter \'{l2}\'")
        sys.exit(1)


save_configuration(sys.argv[1:])
print(f"Configuration saved successfully in {CONFIG_FILE}")

    

