"""
Faça um programa que leia dois números inteiros.
O primeiro é o valor inicial de um contador,
e o segundo é o valor final do contador
(garanta que o valor inicial fornecido é inferior
ao valor final, independente dos valores digitados
pelo usuário). Escreva na tela uma contagem que
comece no primeiro número lido, escreva os números seguintes
colocando apenas um número em cada nova linha da tela,
até chegar ao valor final indicado.
"""

ini = int(input())
fin = int(input())

if ini > fin:
    (ini, fin) = (fin, ini)

for i in range(ini, fin + 1):
    print(i)
