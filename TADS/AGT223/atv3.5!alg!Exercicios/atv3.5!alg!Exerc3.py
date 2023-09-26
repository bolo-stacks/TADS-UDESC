"""
Ler dois números inteiros. Se os números forem iguais,
imprimir a mensagem "Números iguais" e encerrar a execução.
Caso contrário, imprimir o de maior valor.
"""

n1 = int(input())
n2 = int(input())

if n1 == n2:
    print("Números iguais")
elif n1 > n2:
    print(n1)
else:
    print(n2)
