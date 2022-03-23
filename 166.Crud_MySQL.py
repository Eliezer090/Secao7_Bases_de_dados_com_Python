from email import charset
import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(host='192.168.64.2', user='eliezer', password='password',
                              db='clientes', charset='utf8mb4', port=3306, cursorclass=pymysql.cursors.DictCursor)
    try:
        yield conexao
    finally:
        conexao.close()


def executa(sql, parms):
    # com os with abaixo não precisa fechar as conexões, ele fecha automaticamente
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            if isinstance(parms, list):
                cursor.executemany(sql, parms)
            else:
                cursor.execute(sql, parms)
            if sql.upper().startswith('SELECT'):
                return cursor.fetchall()
            else:
                conexao.commit()
                return None


sql = 'insert into clientes (nome, sobrenome, idade, peso) values (%s, %s, %s, %s)'
#print(executa(sql, ('Jack', 'Monroe', 112, 80)))

dados = [('MURIEL', 'Silva', 20, 80),
         ('ROSE', 'Silva', 20, 80),
         ('JOSE', 'Silva', 20, 80)
         ]
#print(executa(sql, dados))

sql = 'delete from clientes where id = %s'
#print(executa(sql, (6,)))

sql = 'delete from clientes where id in (%s, %s, %s)'
#print(executa(sql, (7, 8, 9)))

sql = 'update clientes set nome = %s where id = %s'
#print(executa(sql, ('JOANA', 5)))

sql = 'select * from clientes'
for linha in executa(sql, None):
    print(linha)
