"""
Mostra na tela quantos dígitos
tem no número que o usuário informou
ex: 345 tem 3 dígitos
com log(num) e sem (divisão por 10)
"""

num = int(input('Entre com um numero inteiro:'))
n = num
qtd_dig = 1

# divisão por 10 em loop com contador de loop
# // é divisão de inteiros somente
while n // 10 > 0:
    qtd_dig = qtd_dig + 1
    n = n // 10

print(num, "tem", qtd_dig, "dígitos.")
