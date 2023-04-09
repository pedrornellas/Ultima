
#Escreva um programa que leia 3 lados de um triângulo e mostre qual tipo de triângulo é
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes


def triangulo_tipo (a,b,c):
    if a==b==c:
        print("EQUILÁTERO")
    elif a!=b!=c:
        print ("ESCALENO")
    else:
        print ("ISÓCELES")

triangulo_tipo(3,4,5)
