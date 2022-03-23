import sqlite3


class AgendaDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone, email):
        self.cursor.execute("""
            insert or ignore into agenda (nome, telefone, email)
            values (?, ?, ?);
        """, (nome, telefone, email))
        self.conn.commit()

    def editar(self, nome, telefone, email, id):
        self.cursor.execute("""
            update or ignore agenda set nome = ?, telefone = ?, email = ? where id = ?;
        """, (nome, telefone, email, id))
        self.conn.commit()

    def excluir(self, id):
        self.cursor.execute("""
            delete from agenda where id = ?;
        """, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("""
            select * from agenda;
        """)
        for linha in self.cursor.fetchall():
            identificador, nome, telefone, email = linha
            print(f'{identificador:<4}{nome:<10}{telefone:<20}{email:<20}')

    def fechar(self):
        self.conn.close()

    def create_table_agenda(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS agenda (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL
            );
        """)
        self.conn.commit()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.create_table_agenda()
    #agenda.inserir('João', '123456789', 'joao@123.com')
    #agenda.inserir('Maria', '987654321', 'maria@')
    #agenda.inserir('Pedro', '12349', 'pedro')
    agenda.editar('ROSE', '12345', 'rose@', 6)
    agenda.listar()
    agenda.fechar()
