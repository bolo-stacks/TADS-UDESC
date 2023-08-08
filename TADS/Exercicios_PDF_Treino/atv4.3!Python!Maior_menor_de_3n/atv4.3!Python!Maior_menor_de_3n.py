"""
Escreva um programa que leia três
números e que imprima o maior e o menor.
"""

print('Esse programa mostra o maior e o menor de três números')
num_1 = int(input('Entre com o primeiro número:'))
num_2 = int(input('Entre com o segundo número:'))
num_3 = int(input('Entre com o terceiro número:'))

maior = num_1
if num_2 > num_3 and num_2 > num_1:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3

menor = num_1
if num_2 < num_1 and num_2 < num_3:
    menor = num_2
if num_3 < num_1 and num_3 < num_2:
    menor = num_3

print('O maior número de %d, %d, %d é %d e o menor é %d' % (num_1, num_2, num_3, maior, menor))
