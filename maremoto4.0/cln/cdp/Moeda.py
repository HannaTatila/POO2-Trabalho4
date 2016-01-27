from random import randint
from cln.cdp.Posicao import Posicao

__author__ = 'dell'

class Moeda:

    def __init__(self):
        self.nome = "moeda"
        self.imagem = "moeda.png"
        self.somcolisao = "moeda.wav"
        self.capturou = False
        self.ehtangivel = True
        self.posicaox = 700
        self.posicaoy = randint(150,400)

    def decrementa_posicao_x(self, decremento):
        self.posicaox -= decremento

    def restaura_posicao(self):
        self.posicaox = 700
        self.posicaoy = randint(150,400)
        self.ehtangivel = True

    def torna_intangivel(self):
        self.ehtangivel = False

    def define_posicao(self):
        return Posicao(self.posicaox, self.posicaoy)

    @staticmethod
    def __copy__(self):
        return Moeda()
