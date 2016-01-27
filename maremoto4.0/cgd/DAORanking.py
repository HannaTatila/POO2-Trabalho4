__author__ = 'dell'

import sqlite3

_author__ = 'Hanna e Neimar'


class DAORanking:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("Maremoto.db")  # conexao banco
            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            print("Erro ao abrir o banco.")

    def consultar_banco(self):
        try:
            self.cursor.execute("SELECT login, recorde FROM jogador WHERE recorde <> 0 ORDER BY recorde DESC LIMIT 7")
            return self.cursor.fetchall()
        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao consultar o banco!")

    def fechar_banco(self):
        self.conn.close()
