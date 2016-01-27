import random
import time

import pygame

from cln.cdp.FabricaSprite import FabricaSprite
from cln.cdp.Moeda import Moeda
from cln.cdp.PersonagemMemento import PersonagemMemento
from cln.cdp.Posicao import Posicao
from cln.cdp.tipo.EstadoPersonagem import EstadoPersonagem

_author__ = 'Hanna e Neimar'

class AplJogo:
    def __init__(self):
        self.fabricasprite = FabricaSprite()
        self.personagem = self.fabricasprite.criar_sprite("personagem")
        self.pontos = 0
        self.qtdmoedas = 0
        self.auxpontos = 1
        self.fimdejogo = False
        self.linimigos = ["baiacu", "peixeespada", "peixerapido", "peixeperseguidor"]
        self.lobstaculos = list()
        self.totalobstaculos = 3
        self.limitesuperior = 410
        self.limiteinferior = 40
        self.intervaloobstaculos = 0
        self.menorintervalo = 1.5
        self.maiorintervalo = 2.5
        self.valor_alcance_bonus = 5
        self.tempoinicial = time.clock()

    def configuracao(self):
        self.clock = pygame.time.Clock()

    #cria uma lista de objetos fixa do tipo Moeda ou Esqueleto
    def cria_bloco_bonus(self, qtd, tipo):
        lbonus = list()
        for id in range(qtd):
            lbonus.append(self.fabricasprite.criar_sprite(tipo))
        return lbonus

    def movimenta_personagem(self):
        self.personagem.modifica_posicao(self.personagem.posicao.eixox,
                                         self.personagem.posicao.eixoy + self.personagem.deslocamentoy)

    def gera_novo_intervalo(self):
        self.intervaloobstaculos = random.uniform(self.menorintervalo, self.maiorintervalo)

    def cria_obstaculos(self):
        if (len(self.lobstaculos) < self.totalobstaculos) & (time.clock() - self.tempoinicial > self.intervaloobstaculos or not self.lobstaculos):
                self.tempoinicial = time.clock()
                self.gera_novo_intervalo()
                # Modificar
                obstaculo = self.fabricasprite.criar_sprite(random.choice(self.linimigos))
                if obstaculo.nome == "peixerapido":
                    obstaculo.posicao.eixoy = self.personagem.posicao.eixoy
                self.lobstaculos.append(obstaculo)

    def verifica_limite_da_tela(self):
        self.personagem.atingiu_limite_da_tela()

    def incrementa_pontuacao(self):
        for obstaculo in self.lobstaculos:
            if self.personagem.posicao.eixox > obstaculo.posicao.eixox and self.personagem.posicao.eixox < obstaculo.posicao.eixox + obstaculo.deslocamentox:
                self.pontos += 1
                if self.personagem.estado == EstadoPersonagem.normal:
                    self.auxpontos +=1

    def remove_obstaculo(self):
        for id, obstaculo in enumerate(self.lobstaculos):
            if obstaculo.posicao.eixox < -80:
                del self.lobstaculos[id]

    def testa_colisao_personagem_obstaculo(self, imagempersonagem, imagemobstaculo, obstaculo):
        rectpersonagem = self.captura_rect(imagempersonagem, self.personagem.posicao)
        rectobstaculo = self.captura_rect(imagemobstaculo, obstaculo.posicao).inflate(-50, -50)
        colidiu = rectpersonagem.colliderect(rectobstaculo)
        if colidiu and obstaculo.ehtangivel and not self.personagem.imune:
            obstaculo.torna_intangivel()
            return colidiu
        return False

    # verifica se o personagem colidiu com uma moeda ou um esqueleto
    def testa_colisao_personagem_bonus(self, imagempersonagem, imagembonus, bonus):
        rectpersonagem = self.captura_rect(imagempersonagem, self.personagem.posicao)
        rectmoeda = self.captura_rect(imagembonus, bonus.define_posicao()).inflate(-5, -5)
        colidiu = rectpersonagem.colliderect(rectmoeda)
        if colidiu and bonus.ehtangivel:
            bonus.torna_intangivel()
            return colidiu
        return False

    @staticmethod
    def captura_rect(imagem, posicao):
        return imagem.get_rect().move(posicao.eixox, posicao.eixoy)

    def penaliza_jogador(self):
        self.personagem.vida -= 1

    def verifica_qtd_de_vidas(self):
        if self.personagem.acabou_vida():
            self.fimdejogo = True
            self.personagem.deslocamentoy = 0
            for obstaculo in self.lobstaculos:
                obstaculo.deslocamentox = 0

    def movimenta_obstaculos(self):
        for obstaculo in self.lobstaculos:
            if obstaculo.nome == "peixeperseguidor":
                obstaculo.movimenta(self.personagem.posicao.eixoy, self.personagem.posicao.eixoy)
            else:
                obstaculo.movimenta(self.limitesuperior, self.limiteinferior)

    def verifica_bonus(self):
        if self.qtdmoedas == self.valor_alcance_bonus:
            self.personagem.set_estado_personagem(EstadoPersonagem.motoqueiro, "musicrock.mp3")
            self.personagemmemento = PersonagemMemento(self.personagem)
            self.qtdmoedas = 0
            self.valor_alcance_bonus += self.valor_alcance_bonus

    def jogar(self):
        self.movimenta_personagem()
        self.cria_obstaculos()
        self.movimenta_obstaculos()
        self.incrementa_pontuacao()
        self.remove_obstaculo()
        self.verifica_limite_da_tela()
        self.verifica_qtd_de_vidas()
        self.verifica_bonus()
        pygame.display.flip()
        self.clock.tick(60)