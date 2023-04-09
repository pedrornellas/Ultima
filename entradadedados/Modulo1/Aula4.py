#1) Desenvolva um programa que recebe dados de clientes e armazene-os em uma lista. A saída do seu programa será os dados formatados dos 5 clientes cadastrados.

clientes = []

for cliente in range(5):
  nome  = input()
  cpf   = input()
  idade = int(input())
  
  cadastro_atual = {} 
  cadastro_atual["Nome"]  = nome
  cadastro_atual["CPF"]   = cpf
  cadastro_atual["Idade"] = idade
  clientes.append(cadastro_atual)

for cliente in clientes: 
  print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])

