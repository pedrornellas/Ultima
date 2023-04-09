"""import sqlite3 

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor (id INT, nome VARCHAR(100), endereco VARCHAR(250));')
conexao.commit()
conexao.close()"""


import sqlite3 

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()
cursor.execute('CREATE TABLE cliente (id INT, nome VARCHAR(100), cpf VARCHAR(100), data_cadastro VARCHAR(100), endereco VARCHAR(250));')
conexao.commit()
conexao.close()




"""CREATE TABLE cliente (id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_cadastro DATE NOT NULL,
    endereco TEXT NOT NULL
);

INSERT INTO cliente VALUES (1, 'Danilo', '11111111111', '05/10/2022', 'RIO TINTO');

SELECT * FROM cliente;"""

