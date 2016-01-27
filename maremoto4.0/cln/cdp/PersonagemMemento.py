
__author__ = 'dell'

class PersonagemMemento():

    def __init__(self, personagem):
        self.personagem = personagem
        self.copyofestadoatual = self.personagem.estado
        self.copyofestadoanterior = self.personagem.estadoanterior
        self.copyofmusicaatual = self.personagem.musicaatual
        self.copyofmusicaanterior = self.personagem.musicaanterior

    def restaura_estado(self):
        self.personagem.set_estado_personagem(self.copyofestadoanterior, self.copyofmusicaanterior)
        self.personagem.estadoanterior = self.copyofestadoatual
        self.personagem.musicaanterior = self.copyofmusicaatual


