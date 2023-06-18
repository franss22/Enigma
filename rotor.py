from utils import *

def rotor_connections(type:str):
    # Dado un string de tipo de rotor/refelector, 
    # entrega el diccionario de permutaciones y lista de muescas correspondiente
    raise NotImplementedError


class Rotor:
    connections = {}
    position = 0
    muescas = []

    def rotate(self, places:int):
        next = 0
        if self.position in self.muescas:
            next = 1
        self.position += places
        return next

    def __init__(self, type:str, init_pos:int, _slots:list[int]):
        self.connections, self.muescas= rotor_connections(type)
        self.position = init_pos

        return self

