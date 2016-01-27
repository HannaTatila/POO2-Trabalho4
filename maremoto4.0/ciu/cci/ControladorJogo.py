import os

from pygame.mixer import music
import pygame

from ciu.cih.EventosTeclado import ObservableEventosTeclado
from ciu.cih.Tela import Tela
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.FlyweightFabrica import FlyweightFabrica
from cln.cdp.tipo.EstadoPersonagem import EstadoPersonagem
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador
from cln.cgt.AplJogo import AplJogo
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna e Neimar'

class ControladorJogo:
    TAM_FONTE_TEXTO = 35
    TAM_FONTE_NUMERO = 40
    TAMANHOFONTEGAMEOVER = 40
    DESLOCAMENTO_TELA = 5
    POSICAO_TROCA_TELA = -500
    INTERVALOMOEDAS = 70
    INTERVALOESQUELETOS = 234
    VELOCIDADEBONUS = 11

    def __init__(self):
        self.apljogo = AplJogo()
        self.telajogo = Tela()
        self.aplcadastrarjogador = AplCadastrarJogador()
        self.fabricaimagens = FlyweightFabrica()
        self.imagempersonagem = self.get_imagem("personagem.png")
        self.posicaotela = EstiloElementos.posicao_imagem_fundo()
        self.fundojogo = "fundojogo2.png"
        self.music = False
        self.continuarjogo = True

    @staticmethod
    def get_obstaculo(nomeobstaculo):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_obstaculos(), nomeobstaculo))

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    @staticmethod
    def get_musica(nomemusica):
        return os.path.join(CaminhoRecursos.caminho_musicas(), nomemusica)

    @staticmethod
    def get_som(nomesom):
        return os.path.join(CaminhoRecursos.caminho_sons(), nomesom)

    def exibir_tela_jogo(self):
        imagem = self.get_imagem(self.fundojogo)
        self.telajogo.exibe_imagem(imagem, self.posicaotela)
        self.anda_tela()

    def anda_tela(self):
        self.posicaotela.eixox -= self.DESLOCAMENTO_TELA
        if self.posicaotela.eixox == self.POSICAO_TROCA_TELA:
            self.posicaotela.eixox = 0

    def exibir_vidas(self):
        for numvida in range(self.apljogo.personagem.vida):
            imagem = self.get_imagem("vida.png")
            self.telajogo.exibe_texto("Vida", self.TAM_FONTE_TEXTO, EstiloElementos.posicao_texto_vida())
            self.telajogo.exibe_imagem(imagem, EstiloElementos.get_posicao_vida(numvida))

    def exibir_pontuacao(self):
        self.telajogo.exibe_texto(str(self.apljogo.pontos), self.TAM_FONTE_NUMERO, EstiloElementos.posicao_numero_pontuacao() )
        self.telajogo.exibe_texto("Pontuação", self.TAM_FONTE_TEXTO, EstiloElementos.posicao_texto_pontuacao())

    def exibir_pontuacao_moedas(self):
        self.fabricaimagens.get_flyweight("moeda").desenhar_imagem(EstiloElementos.posicao_desenho_moeda())
        self.telajogo.exibe_texto("Bônus", self.TAM_FONTE_TEXTO, EstiloElementos.posicao_texto_bonus())
        self.telajogo.exibe_texto(str(self.apljogo.qtdmoedas)+" / "+str(self.apljogo.valor_alcance_bonus), self.TAM_FONTE_NUMERO, EstiloElementos.posicao_numero_bonus())

    def exibir_fim_de_jogo(self):
        self.posicaotela.eixox = 0
        imagem = self.get_imagem("gameover.png")
        self.telajogo.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())
        self.telajogo.exibe_texto("Parabéns! Você fez %s pontos"%str(self.apljogo.pontos), self.TAMANHOFONTEGAMEOVER, EstiloElementos.posicao_mensagem_gameover())
        pygame.display.flip()


    def exibir_musica(self, musica):
        self.telajogo.exibe_musica(CaminhoRecursos.caminho_musicas(), musica)

    # exibe moedas e esqueletos na tela
    def exibir_bonus(self, lista, intervalo):
        self.auxbonusanterior = lista[0].posicaox - (intervalo + 1)
        for bonus in lista:
            if ((bonus.posicaox - self.auxbonusanterior) > intervalo) or ((bonus.posicaox - self.auxbonusanterior) < 0):
                bonus.decrementa_posicao_x(self.VELOCIDADEBONUS)
                if bonus.ehtangivel:
                    self.fabricaimagens.get_flyweight(bonus.nome).desenhar_imagem(bonus.define_posicao())
            else:
                break
            self.auxbonusanterior = bonus.posicaox
            if bonus.posicaox <= 0:
                bonus.restaura_posicao()

    def constroi_jogo_evolucao(self):
        self.fabricaimagens.get_flyweight("peixemoto").desenhar_imagem(self.apljogo.personagem.posicao)
        self.exibir_bonus(self.lesqueletos, self.INTERVALOESQUELETOS)
        if not self.music:
            self.music = True
            self.exibir_musica(self.apljogo.personagem.musicaatual)
        self.verifica_colisao_bonus(self.lesqueletos)
        self.fundojogo = "fundojogonegro2.png"

    def constroi_jogo_original(self):
        self.fabricaimagens.get_flyweight("personagem").desenhar_imagem(self.apljogo.personagem.posicao)
        self.exibir_bonus(self.lmoedas, self.INTERVALOMOEDAS)
        self.verifica_colisao_bonus(self.lmoedas)
        self.fundojogo = "fundojogo2.png"

    def exibir_personagem(self):
        if self.apljogo.personagem.estado == EstadoPersonagem.normal:
            self.constroi_jogo_original()
        else:
            self.constroi_jogo_evolucao()

    def atualiza_tela(self):
        self.exibir_tela_jogo()
        self.exibir_personagem()
        for obstaculo in self.apljogo.lobstaculos:
            self.fabricaimagens.get_flyweight(obstaculo.nome).desenhar_imagem(obstaculo.posicao)
        self.exibir_pontuacao()
        self.exibir_vidas()
        self.exibir_pontuacao_moedas()

    # o jogo volta ao estado original (sem motoqueiro)
    def restaura_estado_jogo(self):
        self.apljogo.personagemmemento.restaura_estado()
        self.music = False
        self.exibir_musica(self.apljogo.personagem.musicaatual)

    # verifica se o personagem colidiu com algum obstaculo marinho
    def verifica_colisao_obstaculo(self):
        for obstaculo in self.apljogo.lobstaculos:
            imagemobstaculo = self.get_obstaculo(obstaculo.nome + ".png")
            if self.apljogo.testa_colisao_personagem_obstaculo(self.imagempersonagem, imagemobstaculo, obstaculo):
                self.telajogo.exibe_som(self.get_som(obstaculo.somcolisao))
                if self.apljogo.personagem.estado == EstadoPersonagem.normal:
                    self.apljogo.penaliza_jogador()
                else:
                    self.restaura_estado_jogo()
                    self.restaura_posicao_esqueletos()

    def colidiu_esqueleto(self, objeto):
        self.telajogo.exibe_som(self.get_som(objeto.somcolisao))
        self.restaura_estado_jogo()
        self.restaura_posicao_esqueletos()

    def capturou_moeda(self, objeto):
        self.telajogo.exibe_som(self.get_som(objeto.somcolisao))
        self.apljogo.qtdmoedas += 1

    # verifica se houve colisao do personagem com uma moeda ou um esqueleto
    def verifica_colisao_bonus(self, lista):
        for objeto in lista:
            imagem = self.get_imagem(objeto.imagem)
            if self.apljogo.testa_colisao_personagem_bonus(self.imagempersonagem, imagem, objeto):
                if objeto.nome == "moeda":
                    self.capturou_moeda(objeto)
                else:
                    self.colidiu_esqueleto(objeto)
                    break

    # inicializa a posicao de todos os esqueletos
    def restaura_posicao_esqueletos(self):
        for esqueleto in self.lesqueletos:
            esqueleto.restaura_posicao()

    # a classe ControlodorJogo (q eh um observador)recebe atualização pq a classe Observada ObservableEventosTeclado capturou um evento
    def update(self, observable):
        if observable.cima:
            self.apljogo.personagem.diminui_deslocamento()
        elif observable.soltoubaixo:
            self.apljogo.personagem.aumenta_deslocamento()
        elif (observable.enter) and (self.apljogo.fimdejogo):
            self.continuarjogo = False

    def inicializa_observable(self):
        observable = ObservableEventosTeclado()
        observable.add_observer(self)
        return observable

    def jogo(self, jogador):
        observable = self.inicializa_observable()
        self.exibir_musica(self.apljogo.personagem.musicaatual)
        self.apljogo.configuracao()
        self.lmoedas = self.apljogo.cria_bloco_bonus(11, "moeda")
        self.lesqueletos = self.apljogo.cria_bloco_bonus(3, "esqueleto")
        continua = True
        while continua:
            observable.verifica_evento()
            self.apljogo.jogar()
            self.atualiza_tela()
            self.verifica_colisao_obstaculo()
            if self.apljogo.fimdejogo:
                for moeda in self.lmoedas:
                    moeda.ehtangivel = False
                self.aplcadastrarjogador.cadastrar_pontuacao(jogador, self.apljogo.pontos)
                self.exibir_fim_de_jogo()
                continua = self.continuarjogo
        music.stop()