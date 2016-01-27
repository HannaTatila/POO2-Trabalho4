import sqlite3

_author__ = 'Hanna e Neimar'


class DAOJogador:
    def __init__(self, ldadosjogador):
        self.jogador = ldadosjogador
        try:
            self.conn = sqlite3.connect("Maremoto.db")  # conexao banco
            self.cursor = self.conn.cursor()
            self.criar_tabela()
        except sqlite3.Error:
            print("Erro ao abrir o banco.")


    def criar_tabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS jogador (login varchar(15), senha varchar(8), recorde INTEGER)" )

    def inserir_jogador(self):
        try:
            self.cursor.execute("INSERT INTO jogador (login, senha, recorde) VALUES (?,?,?)", (self.jogador[0], self.jogador[1],0,))
            self.conn.commit()  # salva dados no banco
        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir jogador.")

    def consultar_jogador(self):
        try:
            self.cursor.execute("SELECT login FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
            return len(self.cursor.fetchall()) != 0
        except sqlite3.Error:
            print("Erro ao consultar o banco!")

    def validar_login(self):
        try:
            self.cursor.execute("SELECT login, senha FROM jogador WHERE login = (?) AND senha = ?", (str(self.jogador[0]), str(self.jogador[1]),))
            if len(self.cursor.fetchall()) == 0:
                return False
            else:
                return True
        except sqlite3.Error:
            print("Erro ao consultar o banco para validar login!")

    def atualizar_pontuacao(self, pontos):
        self.cursor.execute("SELECT recorde FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
        tuplarecorde = self.cursor.fetchone()
        if pontos > tuplarecorde[0]:
            self.cursor.execute("UPDATE jogador SET recorde = ? WHERE login = ?", (pontos, self.jogador[0],))
        self.conn.commit()


    def fechar_banco(self):
        self.conn.close()
