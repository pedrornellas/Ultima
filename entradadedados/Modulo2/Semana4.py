import sqlite3

conexao = sqlite3.connect('aulasemana4.db')
cursor = conexao.cursor()

#Criar as tabelas cliente, pedido e item_pedido:

sql_create="""CREATE TABLE IF NOT EXISTS cliente (
  id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome TEXT(100),
  CPF TEXT(14),
  CONSTRAINT client_UN UNIQUE (cpf)
);"""

cursor.execute(sql_create)

sql_pedido="""CREATE TABLE IF NOT EXISTS pedido (
  id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
  data TEXT(20) NOT NULL,
  cliente_id INTEGER NOT NULL,
  CONSTRAINT pedido_FK FOREIGN KEY (client_id) REFERENCES cliente(id)
);"""

cursor.execute(sql_pedido)

sql_item_pedido="""CREATE TABLE IF NOT EXISTS item_pedido (
  id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
  pedido_id INTEGER NOT NULL,
  produto TEXT(100),
  valor REAL,
  quantidade INTEGER,
  CONSTRAINT item_pedido_FK FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);"""

cursor.execute(sql_item_pedido)

conexao.commit()
conexao.close()


#Rotina para inserir dados:

import sqlite3


conexao = sqlite3.connect('aulasemana4.db')
cursor = conexao.cursor()

print("Insira dados dos clientes: ")
nome = input("Qual o nome do cliente? ")
cpf = input("Qual o CPF do cliente? ")
valores = [nome, cpf]
sql_inserir= "INSERT INTO cliente (nome, cpf) VALUES (?, ?)"
cursor.execute(sql_inserir, valores)

conexao.commit()
conexao.close()

#Rotina para inserir clientes:

import sqlite3
import datetime

conexao = sqlite3.connect('aulasemana4.db')
cursor = conexao.cursor()

print("Insira os dados do pedido ")
cliente_id = input("Qual o ID do cliente?")
hoje = datetime.today()
valores = [cliente_id, hoje]
sql_pedido = "INSERT INTO pedido (client_id, data) VALUES (?, ?)"
cursor.execute(sql_pedido, valores)
print ('ID do pedido: ', cursor.lastrowid)

conexao.commit()
conexao.close()

#Rotina para inserir pedidos:

import sqlite3

conexao = sqlite3.connect('aulasemana4.db')
cursor = conexao.cursor()

pedido_id = cursor.lastrowid
quantidade_itens = input ("Quantos itens deseja adicionar? ")
quantidade_itens = int(quantidade_itens)
for i in range(quantidade_itens):
    produto = input('Qual o produto?' )
    quantidade = input('Qual a quantidade? ')
    quantidade = int(quantidade)
    valor = input('Qual o valor? ')
    valor = float(valor)
    sql_item = "INSERT INTO item_pedido (pedido_id, produto, valor, quantidade) VALUES (?, ?, ?, ?)"
    valores = [pedido_id, produto, valor, quantidade]
    cursor.execute(sql_item, valores)

conexao.commit()
conexao.close()
