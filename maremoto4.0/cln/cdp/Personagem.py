from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.tipo.EstadoPersonagem import EstadoPersonagem

_author__ = 'Hanna e Neimar'


class Personagem:
    def __init__(self):
        self.vida = 3
        self.posicao = EstiloElementos.posicao_personagem()
        self.deslocamentoy = 0
        self.imune = False
        self.estado = EstadoPersonagem.normal
        self.estadoanterior = EstadoPersonagem.normal
        self.musicaatual = "music1.mp3"
        self.musicaanterior = "music1.mp3"

    def set_estado_personagem(self, estado, musica):
        self.estadoanterior = self.estado
        self.estado = estado
        self.musicaanterior = self.musicaatual
        self.musicaatual = musica

    def modifica_posicao(self, eixox, eixoy):
        self.posicao.eixox = eixox
        self.posicao.eixoy = eixoy

    def incrementa_vida(self):
        self.vida += 1

    def decrementa_vida(self):
        self.vida -= 1

    def acabou_vida(self):
        return self.vida <= 0

    def aumenta_deslocamento(self):
        self.deslocamentoy = 10 #12

    def diminui_deslocamento(self):
        self.deslocamentoy = -15 #17

    def atingiu_limite_da_tela(self):
        chao = 415
        teto = 50
        # if peixe encostar no chao ou no teto, ele nao ultrapassa a tela
        if self.posicao.eixoy > chao:
            self.posicao.eixoy = chao
        elif self.posicao.eixoy < teto:
            self.posicao.eixoy = teto

    def torna_imune(self):
        self.imune = True

    def torna_desprotegido(self):
        self.imune = False