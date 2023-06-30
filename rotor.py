from utils import *
def rotor_connections(type:str):
    # Dado un string de tipo de rotor/refelector, 
    # entrega el diccionario de permutaciones y lista de muescas correspondiente
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
        muescas=[]
    elif type=='UKW-b':
        con=UKW_B
        muescas=[]
    elif type=='UKW-c':
        con=UKW_C
        muescas=[]
    return (con,muescas)


class Rotor:
    connections = {}
    position = 0
    muescas = []
    
    def __init__(self, rotor, offset):
        con,muescas = rotor_connections(rotor)
        self.connections = con
        self.muescas = muescas
        self.position = offset
        
    def rotate(self, places:int):
        next = 0
        if self.position in self.muescas:
            next = 1
        self.position += places
        
        return next
    
    def input(self, letter:str):
        input_simulado = chr((ord(letter) + self.position - 65) % 26 + 65)
        output_simulado = self.connections[input_simulado]
        output_real = chr((ord(output_simulado) - self.position - 65) % 26 + 65)

        return output_real

    def output(self, letter:str):
        con=self.connections
        output_simulado = chr((ord(letter) + self.position - 65) % 26 + 65)
        input_simulado=list(con.keys())[(list(con.values()).index(output_simulado))]
        input_real=chr((ord(input_simulado) - self.position - 65) % 26 + 65)

        return input_real
    
    def reflect(self, letter:str):
        return self.input(letter)


    # def __init__(self, type:str, init_pos:int, _slots:list[int]):
    #     self.connections, self.muescas= rotor_connections(type)
    #     self.position = init_pos

    #     return self

