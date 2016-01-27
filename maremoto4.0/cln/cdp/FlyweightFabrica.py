from cln.cdp.Sprite import Sprite

_author__ = 'Hanna e Neimar'

class FlyweightFabrica(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FlyweightFabrica, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.flyweights = list()
        #estao no diretorio imagens
        self.flyweights.append(Sprite("personagem.png"))
        self.flyweights.append(Sprite("peixemoto.png"))
        self.flyweights.append(Sprite("moeda.png"))
        self.flyweights.append(Sprite("esqueleto.png"))
        #estao no diretorio obstaculos
        self.flyweights.append(Sprite("peixeespada.png"))
        self.flyweights.append(Sprite("baiacu.png"))
        self.flyweights.append(Sprite("peixerapido.png"))
        self.flyweights.append(Sprite("peixeperseguidor.png"))


    def get_flyweight(self, sprite):
        if sprite == "personagem":
            return self.flyweights[0]
        elif sprite == "peixemoto":
            return self.flyweights[1]
        elif sprite == "moeda":
            return self.flyweights[2]
        elif sprite == "esqueleto":
            return self.flyweights[3]
        elif sprite == "peixeespada":
            return self.flyweights[4]
        elif sprite == "baiacu":
            return self.flyweights[5]
        elif sprite == "peixerapido":
            return self.flyweights[6]
        elif sprite == "peixeperseguidor":
            return self.flyweights[7]