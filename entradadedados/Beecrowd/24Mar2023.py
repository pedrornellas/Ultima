#Exercicio 1006

"""A = float(input())
B = float(input())
C = float(input())

media = (A*2 + B*3 + C*5)/10

print ("MEDIA = {:.1f}".format(media))"""

#Exercicio 1007

"""A = int(input())
B = int(input())
C = int(input())
D = int(input())

Diferenca = (A * B - C * D)

print("DIFERENCA =", Diferenca)"""

#Exercicio 1008

"""num_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas*valor_hora

print ("NUMBER =",num_funcionario)
print ("SALARY = U$ {:.2f}".format(salario))"""

#Exercicio 1009

"""nome_vendedor = str(input())
salario_fixo = float(input())
total_vendas = float(input())

total = salario_fixo+(total_vendas*0.15)

print("TOTAL = R$ {:.2f}".format(total))"""

#Exercicio 1010

"""# leitura dos dados de entrada
codigo_peca_1, numero_peca_1, valor_unitario_1 = input().split()
codigo_peca_2, numero_peca_2, valor_unitario_2 = input().split()

# conversão dos dados para os tipos corretos PS: E se fossem vários entradas? Como "automatizar"??
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

#Exercicio 1011

"""raio = float(input())
pi = 3.14159
volume = (4/3.0)*pi*raio**3

print("VOLUME = {:.3f}".format(volume))"""

#Exercicio 1012

"""# leitura dos valores de A, B e C
a, b, c = map(float, input().split())

# cálculo das áreas
area_tri = a * c / 2
area_circ = 3.14159 * c ** 2
area_trap = (a + b) * c / 2
area_quad = b ** 2
area_ret = a * b

# exibição das áreas calculadas
print("TRIANGULO: {:.3f}".format(area_tri))
print("CIRCULO: {:.3f}".format(area_circ))
print("TRAPEZIO: {:.3f}".format(area_trap))
print("QUADRADO: {:.3f}".format(area_quad))
print("RETANGULO: {:.3f}".format(area_ret))"""