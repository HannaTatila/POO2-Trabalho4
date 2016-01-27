import os
import pygame
from pygame.mixer import music, Sound

_author__ = 'Hanna e Neimar'


class Tela:
    def __init__(self):
        self.branco = (255, 255, 255)
        self.preto = (0, 0, 0)
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.telajogo = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Maremoto")

    def exibe_imagem(self, imagem, posicao):
        self.telajogo.blit(imagem, (posicao.eixox, posicao.eixoy))

    def exibe_texto(self, texto, tamanhofonte, posicao):
        fonte = pygame.font.SysFont("Agency FB", tamanhofonte, False, False)
        text = fonte.render(texto, True, self.branco)
        self.telajogo.blit(text, (posicao.eixox, posicao.eixoy))

    @staticmethod
    def exibe_musica(diretoriomusica, nomemusica):
        music.load(os.path.join(diretoriomusica, nomemusica))
        music.play(-1)

    @staticmethod
    def exibe_som(som):
        som = Sound(som)
        som.play()
