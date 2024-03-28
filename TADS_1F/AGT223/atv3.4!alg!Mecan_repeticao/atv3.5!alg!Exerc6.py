"""
Crie um programa em Python para ler como 
informação de entrada um número inteiro. 
O programa deve somar todos os valores de 1 
até o valor informado. Por exemplo, 
se o usuário entrar com o número 50, 
o programa deverá somar todos os inteiros 
de 1 até 50 (1 + 2 + 3 + ... + 49 + 50).
Veja a resposta abaixo e corrija o algoritmo.
"""

# entrada de dados
n = int(input())

# conta de 1 até n e soma todos os valores
i = 1
soma = 0
while i <= n:
    soma = soma + i
    i = i + 1
# exibe o resultado da soma
print(soma)
