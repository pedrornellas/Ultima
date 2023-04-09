#Faça um Programa que peça dois números e imprima o maior deles.
"""def maiorValor(n1,n2):

    if n1>n2:
        return n1
    elif n1==n2:
        return "Os números possuem o mesmo valor"
    else:
        return n2
print(maiorValor(2,7))"""

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""def valorPositivoOuNegativo (valor):
    if valor>=0:
        return "Positivo"
    else:
        return "Negativo"
print(valorPositivoOuNegativo(-1))"""

##Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
"""def vezesApareceString (string, letra):
    contador = 0
    for item in string:
        if item == letra:
            contador +=1
    
    return contador

print(vezesApareceString("aparece aqui", "a"))"""

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""def verifica_sexo (sexo):

    if sexo.upper() == "F":
        return "F - Feminino"
    elif sexo.upper() == "M":
        return "M - Masculino"
    else:
        return "Sexo Inválido"

sexo = input("Digite o seu sexo (F/M): ")
print (verifica_sexo(sexo))"""

#Testes

"""def calcular_gorjeta(valor_conta):
    gorjeta = valor_conta * 0.1
    return gorjeta

valor_total = float(input("Digite o valor total da conta: "))
valor_gorjeta = calcular_gorjeta(valor_total)

print(f"O valor da gorjeta é R${valor_gorjeta:.2f}, o que representa 10% do valor total da conta.")"""

import math



