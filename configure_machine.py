import sys
from utils import *


available_rotors = ["I", "II", "III", "V", "VI", "VII", "VIII", "Beta"]
available_reflectors = ["UKW-c", "UKW-b"]

def save_configuration(args:list[str]):
    with open(CONFIG_FILE, "w") as config:
        config.write(" ".join(args))
        


if len(sys.argv) < 9:
    print("Wrong amount of arguments")
    sys.exit(1)

rotors = sys.argv[1:5]
for rotor_arg in rotors:
    if rotor_arg not in available_rotors:
        print(f"Rotor argument \"{rotor_arg}\" is not a valid rotor.")
        sys.exit(1)
offsets = []
for offset_arg in sys.argv[5:9]:
    try:
        offsets.append(int(offset_arg))
    except ValueError as e:
        print(f"Offset value \"{offset_arg}\" is not a valid number.")
        sys.exit(1)
reflector = sys.argv[-1]
if reflector not in available_reflectors:
    print(f"Reflector argument \"{reflector}\" is not a valid reflector.")
    sys.exit(1)

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

    

