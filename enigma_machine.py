from utils import *
from rotor import Rotor
import sys

# Configuration is readed
rotors, offsets, plugboard, reflector = read_configuration()

# The message is extracted
length=len(sys.argv)
message=""
for i in range(1,length):
    message=message+sys.argv[i].upper()+" " 
message=message[:-1]

# The rotors and reflector are created
rot1 = Rotor(rotors[0], offsets[0])
rot2 = Rotor(rotors[1], offsets[1])
rot3 = Rotor(rotors[2], offsets[2])
rot4 = Rotor(rotors[3], offsets[3])
refl = Rotor(reflector, 1) # Reflector is always in position 1



encripted= ""
for letter in message:
    #Do not encripts character not in the alphabet
    if ((ord(letter)<ord('A')) or (ord(letter)>ord('Z'))):
        encripted+=letter
    #Encription
    else:
        #each signal passes through the machine
        let = letter

        #the signal is replaced in the plugboard, if it applies
        let = plugboard[let]
    
        #the signal goes through each rotor in one direction
        let = rot1.input(let)
        let = rot2.input(let)
        let = rot3.input(let)
        let = rot4.input(let)

        #the signal is reflected 
        let = refl.reflect(let)

        #and goes through the rotors again in the opposite direction
        let = rot4.output(let)
        let = rot3.output(let)
        let = rot2.output(let)
        let = rot1.output(let)

        #It passes by the plugboard on it's way out
        let = plugboard[let]
    
        #and finally is shown, encrypted
        encripted+= let

        # The first rotor is rotated once after each letter. 
        # if it goes over a notch, the next rotor also rotates, and so on, in a cascading rotation.
        next = rot1.rotate(1)
        next = rot2.rotate(next)
        next = rot3.rotate(next)
        next = rot4.rotate(next)

print(encripted)
