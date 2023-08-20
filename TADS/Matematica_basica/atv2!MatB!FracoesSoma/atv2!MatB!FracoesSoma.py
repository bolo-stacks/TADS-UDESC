"""
Esse programa pede os valores de numerador e denominador
de duas frações e a operação desejada e executa.
"""

# importa o módulo de frações do Python
import fractions

# imprime para o usuário
print('Programa para somar ou multiplicar duas frações')

# pede ao usuário a operação desejada
op = str(input('Insira a operação ( + - * / ) :'))

# pede numerador e denominador das frações
p1 = int(input('Entre com o numerador da primeira fração:'))
q1 = int(input('Entre com o denominador da primeira fração:'))
p2 = int(input('Entre com o numerador da segunda fração:'))
q2 = int(input('Entre com o denominador da segunda fração:'))

# transforma as variáveis em frações
x = fractions.Fraction(p1, q1)
y = fractions.Fraction(p2, q2)

# condicional de processamento
if op == "+":
    sm = x + y
    print(f'A soma das frações {x} e {y} é igual a {sm}.')
elif op == "-":
    sm = x - y
    print(f'A subtração das frações {x} e {y} é igual a {sm}.')
elif op == "*":
    sm = x * y
    print(f'A multiplicação das frações {x} e {y} é igual a {sm}.')
elif op == "/":
    sm = x / y
    print(f'A divisão das frações {x} e {y} é igual a {sm}.')
