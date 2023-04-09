import sqlite3 

conexao = sqlite3.connect('extra.db')

cursor = conexao.cursor()
cursor.execute(
        '''CREATE TABLE IF NOT EXISTS selecao (
                id INTEGER NOT NULL,
                nome VARCHAR(100),
                titulos INTEGER,
                confederacao VARCHAR(100),
                CONSTRAINT selecao_PK PRIMARY KEY(id)          

);'''
)

#Update do titulo Brasil de 5 para 6

sql='''
        UPDATE selecao
        SET titulos = 5
        WHERE nome = 'Brasil';
'''
#Ordenar selecoes por ordem alfabetica

sql='''
        SELECT id, nome, titulos, confederacao FROM selecao ORDER BY nome ASC
'''

#Selecionar selecoes com mais de 3 titulos na tabela

sql='''
        SELECT id, nome, titulos, confederacao FROM selecao WHERE titulos >=3 
'''
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)


conexao.commit()
conexao.close()