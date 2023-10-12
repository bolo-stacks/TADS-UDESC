'''
Exercícios com Matriz valendo nota
'''

# # Exercício 1
# matriz = [[1,2,3], [7,8,9], [5,6,7]]
# valor = matriz[1][1] * matriz[2][2]
# print(valor)


# Exercício 2

# Inicializa a matriz 5x5
# matriz = [[0 for _ in range(5)] for _ in range(5)]

# Valor inicial
# valor = 0

# Preenche a matriz coluna a coluna, começando na primeira linha
# for linha in range(5):
#     for coluna in range(5):
#         matriz[linha][coluna] = valor
#         valor += 1

# Imprime a matriz no formato desejado
# print(matriz)


# Exercício 3


# Inicializa a matriz 5x5
# matriz = [[0 for _ in range(5)] for _ in range(5)]

# Valor inicial
# valor = 0

# Preenche a matriz coluna a coluna, começando na primeira linha
# for linha in range(5):
#     for coluna in range(5):
#         matriz[linha][coluna] = valor
#         valor += 1

# Soma dos valores na matriz
# soma = sum(sum(linha) for linha in matriz)

# Calcula a média
# total_elementos = 5 * 5
# media = soma / total_elementos

# Imprime a soma e a média
# print(soma)
# print(media)


# Exercicio 4

# matriz = [[i * j for j in range(4)] for i in range(5)]
# valores = []

# for _ in range(12):
#     valor = int(input())
#     valores.append(valor)

# for i in range(0, len(valores), 4):
#     linha1, coluna1, linha2, coluna2 = valores[i], valores[i + 1], valores[i + 2], valores[i + 3]
#     matriz[linha1][coluna1], matriz[linha2][coluna2] = matriz[linha2][coluna2], matriz[linha1][coluna1]

# print(matriz)


# Exercício 5

# L = int(input())
# C = int(input())

# matriz = []

# for i in range(L):
#     linha = []
#     for j in range(C):
#         valor = int(input())
#         linha.append(valor)
#     matriz.append(linha)

# print(matriz)
