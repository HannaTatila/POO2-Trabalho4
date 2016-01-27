from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorLogin import ControladorLogin

__author__ = 'dell'


class EstadoMenuIniciar(EstadoMenu):
    MSGDADOINVALIDO = "Os dados informados nao sao validos!"

    def __init__(self, menu):
        self.menu = menu
        self.jogador = ""

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenucadastrar)

    def valor_anterior(self):
        pass

    def selecionar_valor(self):
        telalogin = ControladorLogin()

        telalogin.exibe_tela_informar_dados()
        if telalogin.cadastro():
            self.jogador = telalogin.requisita_jogador()
            controladorjogo = ControladorJogo()
            controladorjogo.jogo(self.jogador)
        else:
            telalogin.exibe_tela_mensagem_cadastro(self.MSGDADOINVALIDO)
            self.menu.aguarda_confirmacao()