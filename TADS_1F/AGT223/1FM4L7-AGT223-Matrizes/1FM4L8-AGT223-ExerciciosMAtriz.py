'''
Exercícios com Matriz valendo nota
'''

# # Exercício 1
# matriz = [[1,2,3], [7,8,9], [5,6,7]]
# valor = matriz[1][1] * matriz[2][2]
# print(valor)


# Exercício 2
'''
Faça um programa em Python para preencher uma matriz M de dimensão 5x5 com uma sequência numérica iniciando em 0 e adicionando valores coluna a coluna iniciando na primeira linha e terminando na quinta, conforme exemplo abaixo:
'''

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

# Versão do professor do exercício 2
# matriz = [[j+(5*i) for j in range(5)] for i in range(5)]
# print(matriz)


# Exercício 3

'''
Faça um programa Python para somar todos os elementos da matriz do exercício anterior e calcular a média dos valores. Exiba ao final uma linha com a soma dos valores (valor inteiro) e outra linha com a média dos valores da matriz com uma casa decimal.
'''

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

# Versão 1 do professor do exercício 3

# matriz = [[j+(i*5) for j in range(5)] for i in range(5)]
# soma = 0
# for i in range(5):
#    soma = soma + sum(matriz[i])
# print(soma)
# print("%.1f" % (soma/25.0))

# Versão 2 do professor do exercício 3

# matriz = [[j+(i*5) for j in range(5)] for i in range(5)]
# soma = 0
# for i in range(5):
#    for j in range(5):
#       soma = soma + matriz[i][j]
# print(soma)
# media = soma/25.0
# print("%.1f" % (media))

# Exercicio 4
'''
Faça um programa para:

    Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices da matriz. Por exemplo, na posição [2][3] será colocado o valor 6 (2x3);
    O programa deve ler 12 valores inteiros, representando 6 posições (e 3 pares de posições). A cada quatro valores, representando duas posições na matriz, faça a troca dos valores na matriz;
    Faça as três trocas (para os 3 pares de posições);
    Mostre a matriz ao final usando print(matriz).

'''

# matriz = [[i * j for j in range(4)] for i in range(5)]
# valores = []

# for _ in range(12):
#     valor = int(input())
#     valores.append(valor)

# for i in range(0, len(valores), 4):
#     linha1, coluna1, linha2, coluna2 = valores[i], valores[i + 1], valores[i + 2], valores[i + 3]
#     matriz[linha1][coluna1], matriz[linha2][coluna2] = matriz[linha2][coluna2], matriz[linha1][coluna1]

# print(matriz)

# Versão do professor do exercício 4

# matriz = [[i*j for j in range(4)] for i in range(5)]
# for i in range(3):
#     l1 = int(input())
#     c1 = int(input())
#     l2 = int(input())
#     c2 = int(input())
#     aux = matriz[l1][c1]
#     matriz[l1][c1] = matriz[l2][c2]
#     matriz[l2][c2] = aux
# print(matriz)

# Exercício 5

'''
Faça um programa para:

    Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices da matriz. Por exemplo, na posição [2][3] será colocado o valor 6 (2x3);
    O programa deve ler 12 valores inteiros, representando 6 posições (e 3 pares de posições). A cada quatro valores, representando duas posições na matriz, faça a troca dos valores na matriz;
    Faça as três trocas (para os 3 pares de posições);
    Mostre a matriz ao final usando print(matriz).

'''

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

# Versão do professor do exercício 5

# matriz = [[i*j for j in range(4)] for i in range(5)]
# for i in range(3):
#     l1 = int(input())
#     c1 = int(input())
#     l2 = int(input())
#     c2 = int(input())
#     aux = matriz[l1][c1]
#     matriz[l1][c1] = matriz[l2][c2]
#     matriz[l2][c2] = aux
# print(matriz)
