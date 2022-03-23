import sqlite3

"""
    Para manipular os registros do SQLITE de uma maneira mais simples, pode ser baixado o 
        sqlitebrowser e usar o mesmo para criar um banco de dados, tabelas, etc.
"""


conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

# cursor.execute("""
#    insert into clientes (nome, telefone, email)
#    values ('João', '123456789', 'joao@mail.com');
# """)

# cursor.execute("""
#    insert into clientes (nome, telefone, email)
#    values ('Maria', '987654321', 'maria@mail.com');
# """)

# Previne SQL injection
# cursor.execute("""
#    insert into clientes (nome, telefone, email)
#    values (?, ?, ?);
# """, ('Pedro', '123456789', 'pedro@mail.com'))

# Pode ser montado um dicionário para passar os valores
# cursor.execute("""
#    insert into clientes (nome, telefone, email)
#    values (:nome, :telefone, :email);
# """, {'nome': 'vitor', 'telefone': '123456789', 'email': 'vitor@mail.com'})

# Update de um registro delete é a mesma coisa é SQL
# curso = cursor.execute("""
#    update clientes set nome = :nome where id = :id;
# """, {'nome': 'gustavo', 'id': 10})

conexao.commit()

# Aqui pode ser feito SQL normal com where order ETC.
cursor.execute("""
    SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    identificador, nome, telefone, email = linha
    print(f'{identificador:<4}{nome:<10}{telefone:<20}{email:<20}')

cursor.close()
conexao.close()
