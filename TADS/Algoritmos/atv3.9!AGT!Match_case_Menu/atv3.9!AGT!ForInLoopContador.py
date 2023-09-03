"""
Contador básico com For in range para relembrar
conta o número de múltiplos de 11 entre 1 e 101.
"""

num = 1
cont = 0
for num in range(1, 101):
    if num % 11 == 0:
        cont = cont + 1

print("São", cont, "múltiplos de 11 entre 1 e 101")

'''
Somar todos os valores em um intervalo.
'''

a = int(input("Início"))
b = int(input("Fim"))
soma = 0

for i in range(a, b + 1):  # b + 1 porque o for conta até o número anterior.
    soma = soma + i  # usa o índice (i) na soma do loop
print('Soma de', a, "até", b, "é", soma)

'''
mesmo programa executando fatorial
'''


d = int(input("Fatorial de:"))
fatorial = 1

for i in range(1, d + 1):  # b + 1 porque o for conta até o número anterior.
    fatorial = fatorial * i  # usa o índice (i) na soma do loop
print(d, '!=', fatorial)
