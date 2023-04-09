"""def somatorio(*args):
  soma = 0
  for numero in args:
    soma += numero
  return soma
print(somatorio(10,9,5,6,3,4))"""


"""def soma_argumentos(numero, numerob, numeroc):
    return numero + numerob + numeroc

print(soma_argumentos(1,5,3))"""

"""def verifica_numero(numero):
    if numero > 0:
       return 'P'
    else:
       return 'N'

numero = int(input())
print(verifica_numero(numero))"""

#

"""var1 = 12

var2 = 30

var3 = var1 + var2

print(var3)

var3 = var3 / 2

print(var3)"""

#

"""x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)"""

#Condicionais If, Elif e Else

"""media  = float(input("Insira a sua média: "))

if media >= 7.0:
    print("Aluno aprovado(a)")
elif media >=5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado(a)")"""

#While

"""numero_sorteado = 13
numero_escolhido = int(input("Insira um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
  print("Não foi dessa vez! Tente novamente informando um novo número")
  numero_escolhido = int(input("Insira um número entre 1 e 20: "))

print("Você acertou o número sorteado! Parabéns")"""

"""contador = 0
while contador <=12:
    print(contador)
    contador = contador + 1"""

"""for variavel in range(int(input("Informe o intervalo aqui: "))):
    
    print(variavel)"""

#For

"""soma = 0
for i in range (1,4):
      nota = (float(input(f"Insira a sua nota {i} aqui: ")))
      soma = soma+nota

print(soma)
media = soma/3

if media >=7:
      print ("Aprovado")
elif media >=5:
      print ("Em recuperação")
else:
      print ("Reprovado")"""

#Listas

"""lista = [1, 10, "Wallison", True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])"""

#Slice

"""lista = [1, 5, 15, 45, 55, 100, 12, 8]

print(lista[0:3])
print(lista[1:7])
print(lista[:6])
print(lista[2:])
print(lista[1::2])"""

# >  Iterando listas com FOR
"""lista = [1, 5, 15, 45, 55, 100, 12, 8]"""

# 1. Utilizando os elementos da própria lista

"""for elementos in lista:
    print(elementos)"""

# 2. Utilizando os índices

"""for i in range (len(lista)):

    print (i, lista[i])"""

# 1. Métodos de Listas

"""lista = [1, 3, 12, 8, 2]

print("Antes do append:", lista)

# 1.1 append

lista.append(3)

print("Após o append: ", lista)

# 1.2 insert

lista.insert(2, 10)

print("Após o insert: ", lista)

# 1.3 extend

lista2 = [1, 2, 3]
lista.extend (lista2)

print("Após o extend: ", lista)

# 1.4 pop

lista.pop()

print("Após o pop: ", lista)

lista.pop(0)

print("Após o pop: ", lista)

# 1.5 remove - Método "remove" remove o primeiro elemento correspondente ao parâmetro passado. Caso haja mais de 1, ele não remove todos.

lista.remove(12)

print("Após o remove: ", lista)

# 1.6 count

print ("Quantidade de elementos 2 na lista: ", lista.count(2))

# 1.7 index

print ("O indice do elemento 2 é: ",lista.index(2))

# 1.8 sort

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# 2. Funcões para Listas

# 2.1 len

print(len(lista))

# 2.2 sum

print(sum(lista))

# 2.3 max

print(max(lista))

# 2.3 min

print(min(lista))"""

#Funcões

# 1. Função Inicial

"""def saudacao():
   
    print(f"Seja bem-vinda(o)!")
    print(f"É um prazer ter você aqui conosco!")

saudacao()"""

# 2. Função com parâmetros

"""def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"É um prazer ter você aqui conosco realizando o curso de {curso}!")

saudacao("Pedro", "Desenvolvedor(a) Python")
saudacao("Juliana", "Analista de Dados")"""

# 3. Função com parâmetros default

"""def saudacao(nome, curso="Desenvolvedor(a) Python"):
    print(f"Seja bem-vinda(o), {nome}!")
    print(f"É um prazer ter você aqui conosco realizando o curso de {curso}!")

saudacao("Pedro")
saudacao("Juliana", "Desenvolvedor(a) Java")"""

# 3. Função com retorno

"""def soma (num1, num2):
    return num1 + num2
resultado = soma(10, 10)

print("O resultado da soma entre os números é:", resultado)"""

"""def calculadora (num1, num2, operador="+"):
    if operador == "+":
        return num1 + num2
    elif operador =="-":
        return num1 - num2
    
resultado = calculadora (50, 50, "+")
print ("O resultado da operação é:", resultado)"""

#Dicionários

#Criando Dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Pedro', 'idade': 36, 'altura':1.70}

print(dicionario)
print(dicionario['idade'])

#Adicionando elementos em um Dicionário

dicionario['programador'] = True
print(dicionario)
dicionario['altura'] = 1.86
print(dicionario)

#Iterando sobre um Dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existência de uma chave


