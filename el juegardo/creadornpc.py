import random
cinco  = random.randint(0,5)


def define_npc():
    velocidad = random.randint(0,3)
    imagen_bebe = cinco
    gustos = cinco
    comida = cinco

    return (velocidad, imagen_bebe, gustos, comida)

print(define_npc())

class Persona:

    def __init__(self, nombre):
        self.name = nombre
        self.estadisticas = []    # creates a new empty list for each dog

    def incstat(self, estadisticas):
        self.estadisticas.append(estadisticas)

d = Persona(input("ingrese un nombre para persona 1: "))
e = Persona(input("ingrese un nombre para persona 2: "))
d.incstat(input('ingrese estadistica: '))
e.incstat(input('ingrese estadistica: '))

print(d.name)
print(e.name)
print(d.estadisticas)
print(e.estadisticas)
