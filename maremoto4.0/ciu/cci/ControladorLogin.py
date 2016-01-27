from ciu.cci.ControladorCadastro import ControladorCadastro

_author__ = 'Hanna e Neimar'


class ControladorLogin(ControladorCadastro):

    def __init__(self):
        super(ControladorLogin, self).__init__()
        self.login = ""

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.validar_login(ldadosjogador)

    def requisita_jogador(self):
        return self.aplcadastrarjogador.requisitar_jogador()