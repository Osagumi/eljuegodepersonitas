import random
cinco  = random.randint(0,5)


def define_npc():
    velocidad = random.randint(0,3)
    imagen_bebe = cinco
    gustos = cinco
    comida = cinco

    return (velocidad, imagen_bebe, gustos, comida)

print(define_npc())

class alquilante:#define las caracteristicas de todos los inquilinos

    def __init__(self, vel, fav, comida):#agregar mas caracteristicas
        self.vel = vel
        self.fav = fav
        self.comida = comida       
    
class persona():#deja definido la persona
    
    def caracters(self):
        return self.vel, self.fav, self.comida #dar un uso extra a esta funcion


class otracosa():

    def caracters(self):
        return True



