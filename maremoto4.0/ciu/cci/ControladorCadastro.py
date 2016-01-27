import os
import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE, K_TAB, QUIT
import sys

from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna e Neimar'


class ControladorCadastro:
    TAMANHO_LETRA_DADOS = 24
    POSICAOX_LETRA_DADOS = 225
    POSICAO_INICIAL_DADOS = 270
    INCREMENTA_ESPACAMENTO = 40
    TAMANHO_PALAVRA = 20

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadastrarjogador = AplCadastrarJogador()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.nomecorrente = []
        self.nome = ""
        self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    def exibe_tela_informar_dados(self):
        imagem = self.get_imagem("teladigitadados.png")
        self.telamenu.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())
        pygame.display.flip()

    def exibe_tela_mensagem_cadastro(self, mensagem):
        imagemtelamensagem = self.get_imagem("telamensagem.png")
        self.telamenu.exibe_imagem(imagemtelamensagem, EstiloElementos.posicao_imagem_fundo())
        self.telamenu.exibe_mensagem_cadastro(mensagem, EstiloElementos.posicao_mensagem_cadastro())
        pygame.display.flip()

    @staticmethod
    def get_key():
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

    def imprime_nome(self, dado, posicaoy):
        self.nome = ""
        for i in range(len(dado)):
            self.nome = self.nome + dado[i]
        self.telamenu.exibe_texto_dados(self.nome, self.TAMANHO_LETRA_DADOS, Posicao(self.POSICAOX_LETRA_DADOS, posicaoy))
        pygame.display.flip()

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.cadastrar_jogador(ldadosjogador)

    def atualiza_entrada(self, ldadosjogador):
        self.exibe_tela_informar_dados()
        posicaoy = self.POSICAO_INICIAL_DADOS
        for dado in ldadosjogador:
            self.imprime_nome(dado, posicaoy)
            posicaoy += self.INCREMENTA_ESPACAMENTO

    def cadastro(self):
        ldadosjogador = []
        while True:
            self.tecla = self.get_key()
            if self.tecla == K_RETURN or self.tecla == K_TAB:
                ldadosjogador.append(self.nome)
                self.nome = ""
                self.nomecorrente = []
                if len(ldadosjogador) == len(self.lopcoes):
                    self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS
                    return self.enviar_dados_jogador(ldadosjogador)
                else:
                    self.posicaoimprimenome = self.posicaoimprimenome + self.INCREMENTA_ESPACAMENTO
            elif self.tecla == K_BACKSPACE:
                if len(self.nomecorrente) > 0:
                    self.nomecorrente.pop(-1)
                    ldadosjogador.append(self.nomecorrente)
                    self.atualiza_entrada(ldadosjogador)
                    ldadosjogador.pop(-1)
            elif self.tecla == K_ESCAPE:
                return []
            elif self.tecla <= 127 and len(self.nomecorrente) < self.TAMANHO_PALAVRA:
                self.nomecorrente.append(chr(self.tecla))
                self.imprime_nome(self.nomecorrente, self.posicaoimprimenome)
