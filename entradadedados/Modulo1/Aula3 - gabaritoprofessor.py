#Crie uma função que, ao receber um número inteiro,
#retorna se um número é par ou ímpar (utilizando **kwargs).
"""def par_ou_impar (**kwargs):
    numero = kwargs["numero"]
    if numero%2 == 0:
        return 'Par'
    else:
        return 'Impar'
resultado = par_ou_impar(numero = 2)
print(resultado)"""

#dic = {"numero": 5}
#print(dic["numera"])
#print(dic.get("numera"))

"""def numero_ate_zero (numero):
    if numero == 0:
        return 0
    print(numero)
    return numero_ate_zero(numero-1)
numero = int(input())
print(numero_ate_zero(numero))"""

"""
def somatorio (*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma
print( somatorio(10,9,5,6,3,4) )
"""

"""def validacao_argumento (argumento):
    if argumento > 0:
        print("P")
    else:
        print("N")
numero = int(input())
validacao_argumento(numero)"""

"""def vezesLetraAparece (string, letra):
    contador = 0
    for item in string:
        if item == letra:
            contador +=1
    return contador
print (vezesLetraAparece("paralelepipedo", "p"))"""

"""def calcula_gorjeta(conta):
    gorjeta = conta*0.1
    return gorjeta
valor = float(input())
print(calcula_gorjeta(valor))"""

""" Versão 1: fazendo tudo do zero
def verifica_prefixo(palavra, prefixo):
    tamanho = len(prefixo)
    for i in range( tamanho ):
        if palavra[i] != prefixo[i]:
            return False
    return True
#Indices   01234
palavra = "Pedro"
prefixo = "Pedro"
print(verifica_prefixo(palavra, prefixo))"""

"""Versão 2: utilizando recursos do python
def verifica_prefixo(palavra, prefixo):
    return prefixo == palavra[0: len(prefixo)]
print(verifica_prefixo("para", "paralelepipedo"))"""