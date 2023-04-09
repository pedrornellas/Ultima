"""idade = int(input("Insira a sua idade: "))

if idade >= 18:
    print ("Pode ir se alistar!")
else:
    print ("Aproveite a vida enquanto pode!")"""


"""velocidade = int(input("Insira a leitura de velocidade: "))

if velocidade < 50:
    print ("Baixa velocidade")
elif velocidade < 100:
    print ("Velocidade Moderada")
else:
    print ("Carai, Biridin!")"""

"""nomes = ["José", "Clarice", "Joaquim", "Maria", "Carlucci", "Marilene", "Letícia"]"""

"""nome_com_mais_de_5_chars = [nome for nome in nomes if len(nome) <=5]
print(nome_com_mais_de_5_chars)"""

"""alunos = ["Elisson", "Giulia", "Pedro", "Amanda", "Lucia"]

alunos_presentes=0

for aluno in alunos:
    print ('{} presente!'.format(aluno))
    alunos_presentes +=1

print ("Quantidade de alunos presentes ".format(alunos_presentes))

print([aluno.upper() for aluno in alunos])"""

"""nome_com_mais_de_5_chars = []

for nome in nomes:
    if len(nome)>=5:
        nome_com_mais_de_5_chars.append(nome)

print([nome.upper() for nome in nome_com_mais_de_5_chars])"""

"""for numero in range (1000):
    if numero %2 !=0:
        continue
    print(f'Número {numero} é par!')"""

"""coordenadas = [
    (1,1),
    (2,1),
    (3,4)
]

for x,y in coordenadas:
    print (f'X: {x} | Y: {y}')"""

"""soma = 0

while soma < 100:
    soma +=5
    if soma%2 != 0:
        print(f'Soma é igual a {soma} e é um número ímpar!')
    else:
        print(f'Soma é igual a {soma}!')"""

"""combinacoes = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

for x, y in combinacoes:
    print(f'{x} AND {y} -> {x == y}')"""

"""numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

resultado1 = (numero1*2) * (numero2/2)
resultado2 = (numero1*3) + numero2
resultado3 = numero2 ** 3

print ('O resultado 1 é: {:.0f}' .format(resultado1))
print ('O resultado 1 é: {:.0f}' .format(resultado2))
print ('O resultado 1 é: {:.0f}' .format(resultado3))"""

"""cinco_centavos = int(input("Insira quantidade de moedas de 5 centavos: "))
dez_centavos = int(input("Insira quantidade de moedas de 10 centavos: "))
vintecinco_centavos = int(input("Insira quantidade de moedas de 25 centavos: "))
cinquenta_centavos = int(input("Insira quantidade de moedas de 50 centavos: "))
um_real = int(input("Insira quantidade de moedas de 1 real: "))"""

"""soma_cincocentavos = 35*0.05
soma_dezcentavos = 50*0.10
soma_vintecincocentavos = 30*0.25
soma_cinquentacentavos = 15*0.50
soma_umreal = 19*1.0

somatório = (soma_cincocentavos+soma_dezcentavos+soma_vintecincocentavos+soma_cinquentacentavos+soma_umreal)

print (f'{somatório:.2f}')"""

"""# (valor inicial + quantidade de horas estimadas * valor da hora) + 15% do valor calculado
# (1000          + 80                            * 20.45        ) + 0.15*(1000+80*20.45)

valor_calculado = 1000+(80*20.45)
valor_projeto = valor_calculado+(0.15*valor_calculado)

print (f'O valor do projeto é: R$ {valor_projeto:.2f}')"""


# Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo nome lido na lista e imprimindo a frase de boas vindas com o
# nome substituído.

nomes = ["Elysson", "Giulia", "Willian", "Gileno"]

for nome in nomes:
    
    print(f'Olá, {nome}! Seja bem vindo à nave Imperial dos Siths.')


