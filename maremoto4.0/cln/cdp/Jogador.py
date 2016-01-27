__author__ = 'dell'

class Jogador():

    def __init__(self):
        self.login = ""
        self.pontuacao = 0

    def set_login(self, login):
        self.login = login

    def altera_pontuacao(self, pontos):
        self.pontuacao = pontos
