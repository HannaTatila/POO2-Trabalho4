from cgd.DAOJogador import DAOJogador
from cgd.DAORanking import DAORanking
from cln.cdp.Jogador import Jogador

_author__ = 'Hanna e Neimar'


class AplCadastrarJogador:

    @staticmethod
    def cadastrar_jogador(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        jogadorexiste = jog.consultar_jogador()
        if not jogadorexiste:
            jog.inserir_jogador()
        jog.fechar_banco()
        return not jogadorexiste


    def validar_login(self, ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        if jog.validar_login():
            jog.fechar_banco()
            self.inicializar_jogador(ldadosjogador)
            return True
        else:
            return False

    def inicializar_jogador(self, ldadosjogador):
        self.jogador = Jogador()
        self.jogador.set_login(ldadosjogador)

    def requisitar_jogador(self):
        return self.jogador

    @staticmethod
    def cadastrar_pontuacao(jogador, pontos):
        jog = DAOJogador(jogador.login)
        jog.atualizar_pontuacao(pontos)

    @staticmethod
    def buscar_ranking():
        ranking = DAORanking()
        lrecordes = ranking.consultar_banco()
        ranking.fechar_banco()
        return lrecordes
