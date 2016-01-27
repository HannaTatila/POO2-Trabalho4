import os
import pygame
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador
from principal.CaminhoRecursos import CaminhoRecursos

__author__ = 'dell'

class ControladorRanking:
    TAMFONTETEXTO = 35
    POSICAOXNOME = 105
    POSICAOXPONTUACAO = 480
    ESPACAMENTONOMES = 43
    POSICAOYLINHA = 188

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadjog = AplCadastrarJogador()

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    def exibir_tela_ranking(self):
        imagem = self.get_imagem("telaranking.png")
        self.telamenu.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())

    def imprimir_ranking(self, lrecordes):
        posicaoylinha = self.POSICAOYLINHA
        for linha in lrecordes:
            self.telamenu.exibe_texto(str(linha[0]), self.TAMFONTETEXTO, Posicao(self.POSICAOXNOME, posicaoylinha))
            self.telamenu.exibe_texto(str(linha[1]), self.TAMFONTETEXTO, Posicao(self.POSICAOXPONTUACAO, posicaoylinha))
            posicaoylinha += self.ESPACAMENTONOMES

    def retorna_ranking(self):
        self.exibir_tela_ranking()
        lrecordes = self.aplcadjog.buscar_ranking()
        self.imprimir_ranking(lrecordes)
        pygame.display.flip()



