#Exercicio 1040 

"""# lê as notas do aluno
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
    
    print ("Media final:", media_final)"""


#Exercicio 1010

"""# leitura dos dados de entrada
codigo_peca_1, numero_peca_1, valor_unitario_1 = input().split()
codigo_peca_2, numero_peca_2, valor_unitario_2 = input().split()

# conversão dos dados para os tipos corretos #PS: E se fossem vários entradas? Como "automatizar"??
codigo_peca_1 = int(codigo_peca_1)
numero_peca_1 = int(numero_peca_1)
valor_unitario_1 = float(valor_unitario_1)

codigo_peca_2 = int(codigo_peca_2)
numero_peca_2 = int(numero_peca_2)
valor_unitario_2 = float(valor_unitario_2)

# cálculo do valor a ser pago
valor_total = numero_peca_1 * valor_unitario_1 + numero_peca_2 * valor_unitario_2

# impressão dos resultados
print("VALOR A PAGAR: R$ {:.2f}".format(valor_total))"""

#Exercicio 1013

"""a, b, c = map(int, input().split())

maior_ab = (a + b + abs(a - b)) // 2
maior_abc = (maior_ab + c + abs(maior_ab - c)) // 2

print(maior_abc, "eh o maior")"""

#Exercicio 1018

"""valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
contador = 0

print(valor)

for nota in notas:
    quantidade = valor // nota
    contador += quantidade
    valor -= quantidade * nota
    print(f"{quantidade} nota(s) de R$ {nota},00")"""

