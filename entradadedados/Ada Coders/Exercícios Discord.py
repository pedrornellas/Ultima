#Faça um programa que peça ao usuário um número e imprima todos os números de um até o número que o usuário informar.
#NH

"""contador = 0
for i in range(int(input("Insira aqui seu número: "))):
    contador=contador+1
    print(contador)"""

#2

"""numero = float(input('Informe um número: '))

if numero < 0 or numero > 100:
  print('Fora de intervalo')
elif numero <= 25:
  print('[0, 25]')
elif numero <= 50:
  print('(25, 50]')
elif numero <= 75:
  print('(50,75]')
else:
  print('(75,100]')"""

#3
#NH

"""import math
def calcular_area_circulo():

    raio = float(input('Insira o raio do círculo: '))
    area_do_circulo = math.pi*(raio**2)
    return area_do_circulo

print(f'A área do círculo é de {calcular_area_circulo():.4f}')"""

#4
#NH

"""def calculadora(numint1, numint2, numreal):

    numint1 = int(numint1)
    numint2 = int(numint2)
    numreal = float(numreal)

    print (numint1*2)*(numint2/2)
    print (numint1*3)+(numreal)
    print (numreal**3)

    return calculadora

print(calculadora(5,4,1.5))"""

#5

"""#Perguntas para os suspeitos

pergunta1 = (input('Mora perto da vítima? ')).lower()
pergunta2 = (input('Já trabalhou com a vítima? ')).lower()
pergunta3 = (input('Telefonou para a vítima? ')).lower()
pergunta4 = (input('Esteve no local do crime? ')).lower()
pergunta5 = (input('Devia para a vítima? ')).lower()

#Somatório das Respostas

soma_respostas=0
if pergunta1 == 'sim':
    soma_respostas=soma_respostas+1
if pergunta2 == "sim":
    soma_respostas=soma_respostas+1
if pergunta3 == 'sim':
    soma_respostas=soma_respostas+1
if pergunta4 == "sim":
    soma_respostas=soma_respostas+1
if pergunta5 == "sim":
    soma_respostas=soma_respostas+1

print(soma_respostas)

#Resultado do Suspeito

if soma_respostas < 2:
    print ("Inocente")
elif soma_respostas == 2:
    print ("Suspeito")
elif soma_respostas == 3 or soma_respostas==4:
    print ("Cúmplice")
else:
    print("Assassino")"""

#6 Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
#NH

"""def soma_lista(lista):
    soma=0
    for elementos in lista:
        soma=soma+elementos
    return soma

lista=[2,3,5,10]
resultado = soma_lista(lista)

print ("O resultado da soma dos elementos da lista é =",resultado)"""



















