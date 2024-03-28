"""
Faça um programa para calcular o fatorial de um número. 
A entrada do programa é um valor inteiro e a saída
mostra o número e seu fatorial (5! = 120).
"""

num = int(input())
ft = 1
for i in range(1, num + 1):
    ft = ft * i
    i = i + 1
print('%d! = %d' % (num, ft))
