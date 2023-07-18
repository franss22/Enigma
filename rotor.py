from utils import *

def rotor_connections(type:str):
    # Given a string that represent a rotor o reflector, return the dictionary associated according to documentation
    if type=='I':
        con=I
        muescas=[24]
    elif type=='II':
        con=II
        muescas=[12]
    elif type=='III':
        con=III
        muescas=[3]
    elif type=='IV':
        con=IV
        muescas=[17]
    elif type=='V':
        con=V
        muescas=[7]
    elif type=='VI':
        con=VI
        muescas=[7,20]
    elif type=='VII':
        con=VII
        muescas=[7,20]
    elif type=='VIII':
        con=VIII
        muescas=[0,21]
    elif type=='Beta':
        con=BETA
        muescas=[] # Beta is always in last position of the rotors, It doesn't rotate (It can´t do a rotation cascade)
    elif type=='UKW-b':
        con=UKW_B
        muescas=[] # Reflector doesn´t rotate, It can´t do a rotation cascade
    elif type=='UKW-c':
        con=UKW_C
        muescas=[] # Reflector doesn´t rotate, It can´t do a rotation cascade
    return (con,muescas)

# Representation of a rotor, with its attributes, this class can representate a reflector
class Rotor:
    
    def __init__(self, rotor, offset):
        con,muescas = rotor_connections(rotor)
        self.connections = con
        self.muescas = muescas
        self.position = offset-1 # the logic of the encryption implementation starts in 0, so we have to do this arrangement
        
    def rotate(self, places:int):
        next = 0
        if places!=0: # if the rotor rotates
            if self.position in self.muescas: # if there is a notch
                next = 1 # the next rotor rotates
            self.position += places # the actual rotor rotates
        return next
    
    def input(self, letter:str):
        # translation of the letter according to the simulation of the machine
        input_simulado = chr((ord(letter) + self.position - 65) % 26 + 65)
        output_simulado = self.connections[input_simulado]
        output_real = chr((ord(output_simulado) - self.position - 65) % 26 + 65)

        return output_real

    def output(self, letter:str):
        # translation of the letter according to the simulation of the machine
        con=self.connections
        output_simulado = chr((ord(letter) + self.position - 65) % 26 + 65)
        input_simulado=list(con.keys())[(list(con.values()).index(output_simulado))]
        input_real=chr((ord(input_simulado) - self.position - 65) % 26 + 65)

        return input_real
    
    # reflector works like a rotor
    def reflect(self, letter:str):
        return self.input(letter)
