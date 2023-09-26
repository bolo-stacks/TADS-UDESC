"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada
"""

print("Calculadora básica")

op = input('Entre com a operação a ser realizada\n(+, -, *, /):')
n1 = float(input("Entre com o primeiro número:"))
n2 = float(input("Entre com o segundo número:"))

if op == "+":
    res = n1 + n2
elif op == "-":
    res = n1 - n2
elif op == "*":
    res = n1 * n2
elif op == "/":
    res = n1 / n2
else:
    print('Operação inválida!')
    res = 0
print("O resultado da %s entre %.2f e %.2f é: %.2f" % (op, n1, n2, res))
