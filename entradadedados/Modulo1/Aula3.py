"""def apresentacoes(nome):
    print("Olá", nome)"""


"""def apresentacoes (nome, idade):
    return print('Olá', nome, '\nSua idade é: ', idade)

apresentacoes("Pedro", 36)"""

"""def mistura_palavras (*args):
    return '_' .join(args)

print(mistura_palavras("Tu", "é", "Comedião"))"""

"""def fatorial (numero):
    if numero == 1:
        return 1
    
    return numero * fatorial (numero-1)

print (fatorial (5))"""

#1) Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar (utilizando **kwargs).

def par_ou_impar (**kwargs):

    numero = kwargs['numero']
    
    if numero%2 == 0:
        print ('Par')
    else:
        print ('Impar')

        return par_ou_impar(numero)
    
par_ou_impar(numero=2)

#2) Crie de forma recursiva uma função que printe do número recebido até o zero.

def funcao(x):
    if x >= 0:
        print(x)
        funcao(x-1)

numero = int(input())
funcao(numero)

#3) Crie uma função de somatório que some todos os números que a função receber (usando *args)

def somatorio (numero1, numero2, numero3):

    return numero1+numero2+numero3

print(somatorio (15,15,7))

#4) Crie um programa com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somatorio (numero1, numero2, numero3):

    return numero1+numero2+numero3

print(somatorio (3,3,3))

#5) Faça um programa com uma função que necessite de um argumento. A função deve retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verifica_numero(numero):
    if numero > 0:
       return 'P'
    else:
       return 'N'

numero = int(input())
print(verifica_numero(numero))

#6) Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.

def vezesLetraAparece (string, letra):
    contador = 1
    for item in string:
        if item == letra:
            contador +=1
    return contador
print (vezesLetraAparece("Aparece aqui", "a"))

#7) Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

def calcula_gorjeta(conta):
    gorjeta = conta*0.1
    return gorjeta

print(calcula_gorjeta(1000))    

#8)Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda.
#Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.

def check_prefixo (prefixo, palavra):
    tamanho = len (prefixo)
    return prefixo == palavra [:tamanho]
    
print(check_prefixo("lag", "lagartixa"))
        


