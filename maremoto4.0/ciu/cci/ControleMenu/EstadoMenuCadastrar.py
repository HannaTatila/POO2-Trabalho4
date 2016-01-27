from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorCadastro import ControladorCadastro

__author__ = 'dell'

class EstadoMenuCadastrar(EstadoMenu):
    MSGSUCESSO = "Jogador cadastrado com sucesso!"
    MSGERRO = "Login informado ja existe!"

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenucreditos)

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenuiniciar)

    def selecionar_valor(self):
        telacadastro = ControladorCadastro()

        telacadastro.exibe_tela_informar_dados()
        if telacadastro.cadastro():
            telacadastro.exibe_tela_mensagem_cadastro(self.MSGSUCESSO)
        else:
            telacadastro.exibe_tela_mensagem_cadastro(self.MSGERRO)
        self.menu.aguarda_confirmacao()
