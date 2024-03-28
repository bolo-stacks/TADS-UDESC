"""
Faça um programa em Python para fazer a
média de vários valores indicados pelo usuário.
O usuário entra primeiramente com a quantidade
de valores e em seguida a sequência de valores (tipo float).
A saída do programa é a média de todos os valores.
"""

n = int(input())
notas = []
soma = 0

for i in range(n):
    nota = float(input())
    notas.append(nota)
    soma += nota

media = soma / n
print('%.15f' % media)

'''
Versão do professor
'''

# Trecho de Código: Média de n valores (Python)
# Entre com o valor de elementos

n = int(input())

# calcula a média

media = 0.0
for i in range(n):
    media = media + float(input())
media = media / n

# Saída: imprime a média
print(media)
