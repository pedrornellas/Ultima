#Exercicio 1001

"""A = int(input())
B = int(input())
X = A+B
print("X =",X)"""

#Exercicio 1002

"""n = 3.14159
raio = float(input())
area = n*raio**2
print ("A={:.4f}".format(area))"""

#Exercicio 1003

"""A = int(input())
B = int(input())
SOMA=A+B
print ("SOMA =",SOMA)"""

#Exercicio 1004

"""A = int(input())
B = int(input())
PROD=A*B
print ("PROD =",PROD)"""

#Exercicio 1005

"""A = float(input())
B = float(input())

media = (A*3.5 + B*7.5)/11

print ("MEDIA = {:.5f}".format(media))"""

#Exercicio 1040 

# lê as notas do aluno
N1, N2, N3, N4 = map(float, input().split())


# calcula a média ponderada das notas
media = (N1*2 + N2*3 + N3*4 + N4*1) / 10

# imprime a média com duas casas decimais
print('Media: {:.1f}'.format(media))

# verifica se o aluno foi aprovado, reprovado ou está em exame
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    
    # lê a nota do exame
    exame = float(input())
    
    # recalcula a média ponderada com a nota do exame
    media_final = (media + exame) / 2
    
    # imprime a nota do exame e a média final com duas casas decimais
    print('Nota do exame: {:.1f}'.format(exame))
    print('Media final: {:.1f}'.format(media_final))
    
    # verifica se o aluno foi aprovado ou reprovado após o exame
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print ("Media final:", media_final)