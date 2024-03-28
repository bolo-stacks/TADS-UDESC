"""
Soma de ímpares, versão do bing assistente.
"""

N = int(input())

for i in range(N):
    linha = [int(num) for num in input().split()]
    X = min(linha)
    Y = max(linha)
    soma = 0
    for num in range(X + 1, Y):
        if num % 2 == 1:
            soma += num
    print(soma)



# Minha versão alterada do Bing
# Ainda não está funcionando.
'''
N2 = int(input())
linha2 = []
for i2 in range(N2):
    n1 = int(input())
    n3 = int(input())
    linha2.append(n1)
    linha2.append(n3)
    X1 = min(linha2)
    Y1 = max(linha2)
    soma2 = 0
    for num2 in range(X1 + 1, Y1):
        if num2 % 2 == 1:
            soma2 += num2
    print(soma2)
    linha2.clear()
'''