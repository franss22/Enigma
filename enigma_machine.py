from utils import *
from rotor import Rotor

rotors, offsets, plugboard, reflector = read_configuration()
print(rotors, offsets, plugboard, reflector)

message = "alshgkjfgsdfkhsdf".upper()

rot1 = Rotor(rotors[0], offsets[0])
rot2 = Rotor(rotors[1], offsets[1])
rot3 = Rotor(rotors[2], offsets[2])
rot4 = Rotor(rotors[3], offsets[3])




encripted= ""
for letter in message:
    let = letter
    let = plugboard[let]
    let = rot1.input(let)
    let = rot2.input(let)
    let = rot3.input(let)
    let = rot4.input(let)

    let = reflector.reflect(let)

    let = rot4.output(let)
    let = rot3.output(let)
    let = rot2.output(let)
    let = rot1.output(let)

    let = plugboard[let]
    encripted+= let

    next = rot1.rotate(1)
    next = rot2.rotate(next)
    next = rot3.rotate(next)
    next = rot4.rotate(next)

print(encripted)
