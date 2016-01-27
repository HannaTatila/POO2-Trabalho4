import copy
from cln.cdp.Esqueleto import Esqueleto
from cln.cdp.Moeda import Moeda
from cln.cdp.Personagem import Personagem
from cln.cdp.inimigo.Baiacu import Baiacu
from cln.cdp.inimigo.PeixeEspada import PeixeEspada
from cln.cdp.inimigo.PeixePerseguidor import PeixePerseguidor
from cln.cdp.inimigo.PeixeRapido import PeixeRapido

_author__ = 'Hanna e Neimar'


class FabricaSprite():
    def __init__(self):
        self.peixeespada = PeixeEspada()
        self.baiacu = Baiacu()
        self.peixeperseguidor = PeixePerseguidor()
        self.peixerapido = PeixeRapido()
        self.moeda = Moeda()
        self.esqueleto = Esqueleto()

    def criar_sprite(self, tipo):
        sprite = None
        if tipo == "peixeespada":
            sprite = copy.copy(self.peixeespada)
        elif tipo == "baiacu":
            sprite = copy.copy(self.baiacu)
        elif tipo == "peixerapido":
            sprite = copy.copy(self.peixerapido)
        elif tipo == "peixeperseguidor":
            sprite = copy.copy(self.peixeperseguidor)
        elif tipo == "personagem":
            sprite = Personagem()
        elif tipo == "moeda":
            sprite = copy.copy(self.moeda)
        elif tipo == "esqueleto":
            sprite = copy.copy(self.esqueleto)
        return sprite
