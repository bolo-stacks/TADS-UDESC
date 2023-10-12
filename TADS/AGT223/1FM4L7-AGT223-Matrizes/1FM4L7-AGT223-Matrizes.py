import random
import random


# Algoritmos dos slides


'''
Criar um vetor de 8 números inteiros, 
composto de múltiplos de 3, iniciando pelo
valor 15.
Imprimir
'''

# vetor = [0] * 8
# for i in range(8):
# vetor[i] = 15 + (i*3)
# print(vetor)


'''
Algoritmo que dada uma matriz de 3x3,
armazene em cada posição da matriz, a soma dos valores
da linha e coluna que definem a posição, [1][2] você 
deverá armazenar o valor 1+2=3 e assim por diante.
Exiba esta matriz uma linha abaixo da outra
'''

# matriz = [0,0,0],[0,0,0],[0,0,0]
# for i in range(3):
#     for j in range(3):
#         matriz[i][j] = i+j
#     print(matriz[i])

'''
Método de construção de listas compreensão |(lists comprehensions)
'''
# i é o número de itens na lista (10)

# lista = [i*10 for i in range(1,10)]
# print(lista)

'''
2° exemplo de lists comprehensions
'''

# lista = [i*10 for i in range(1,19) if i%2==0]
# print(lista)

'''
3° exemplo de lists comprehensions
'''

# i é o número de ítens dentro da matriz e j é o numero da matriz[itens, matrizes]

# matriz = [[i+j for j in range(3)] for i in range(1,10,3)]
# print(matriz)

'''
Crie uma matriz identidade de tamanho 5x5
'''

# matriz = [[1 if i==j else 0 for j in range(5)] for i in range(5)]
# for i in range(5):
#     print(matriz[i])


'''
Lista de listas
'''

# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(3):
#     for j in range(3):
#         matriz[i][j]=i+j
# print(matriz[i])

'''
Exercício 1:

Faça um programa que preencha uma matriz de 20x3 com as notas de vinte alunos em três provas (complete com valores aleatórios de 0 a 10 para evitar a leitura de muitos valores).
O programa deve mostrar em que posição aparecem as menores notas para: prova 1, prova 2 e prova 3. Exiba a posição e a nota.
'''

# import random
# Minha versão que ainda não funciona:

# matriz = [[random.randint(0, 10) if i != j else random.randint(0, 10)
#            for j in range(20)] for i in range(3)]
# posnota = []
# repetidos = []

# print("\n", matriz, "\n")

# for j in range(3):
#     for i in range(20):
#         menor = (min(matriz[j]))
#         pos = matriz[j].index(menor)
#         for menor in matriz[j]:
#             if pos not in posnota:
#                 posnota.append(menor)
#                 posnota.append(pos)
#             else:
#                 repetidos.append(menor)
#                 repetidos.append(pos)
#             # pos = matriz[j].index(menor)
#             # posnota.append([menor, pos])

# print(posnota)


# Versão do ChatGPT

# Função para preencher a matriz com notas aleatórias de 0 a 10
# def preencher_matriz_notas():
#     matriz = []
#     for _ in range(20):
#         aluno = [random.randint(0, 10) for _ in range(3)]
#         matriz.append(aluno)
#     return matriz

# Função para encontrar a posição e o valor da menor nota em uma prova específica
# def menor_nota_prova(matriz, prova):
#     menor_nota = matriz[0][prova]
#     posicao = (0, prova)
#     for i in range(len(matriz)):
#         if matriz[i][prova] < menor_nota:
#             menor_nota = matriz[i][prova]
#             posicao = (i, prova)
#     return posicao, menor_nota

# Preencher a matriz de notas
# matriz_notas = preencher_matriz_notas()

# Encontrar a posição e a menor nota para cada prova
# for prova in range(3):
#     posicao, nota = menor_nota_prova(matriz_notas, prova)
#     print(f"Menor nota na prova {prova + 1} - Posição: {posicao}, Nota: {nota}")


'''
Exercício 2:

Escreva um algoritmo que gera uma matriz 7x7 preenchida com valores aleatórios (randômicos) de 0 a 100. Escreva a matriz na tela e os seguintes valores:
- Posição (linha e coluna) onde está o maior valor.
- Quantas vezes o maior valor aparece (Inclui repetições).
- Posição onde está o menor valor.
- Quantas vezes o menor valor aparece.
'''

# Minha versão:

# matriz = [[random.randint(0, 100) if i != j else random.randint(0, 100)
#            for j in range(7)] for i in range(7)]
# posnota = []
# repetidos = []

# print(matriz)
# menor = (min(matriz))
# maior = (max(matriz))

# for j in range(7):
#     for i in range(7):


# Função para preencher a matriz 7x7 com valores aleatórios de 0 a 100
# def preencher_matriz():
#     matriz = [[random.randint(0, 100) for _ in range(7)] for _ in range(7)]
#     return matriz

# Função para encontrar a posição do maior e do menor valor na matriz
# def encontrar_maior_menor(matriz):
#     maior_valor = menor_valor = matriz[0][0]
#     maior_posicao = menor_posicao = (0, 0)
#     contagem_maior = contagem_menor = 1

#     for i in range(7):
#         for j in range(7):
#             valor = matriz[i][j]

#             if valor > maior_valor:
#                 maior_valor = valor
#                 maior_posicao = (i, j)
#                 contagem_maior = 1
#             elif valor == maior_valor:
#                 contagem_maior += 1

#             if valor < menor_valor:
#                 menor_valor = valor
#                 menor_posicao = (i, j)
#                 contagem_menor = 1
#             elif valor == menor_valor:
#                 contagem_menor += 1

#     return maior_posicao, contagem_maior, menor_posicao, contagem_menor

# Função para exibir a matriz na tela
# def exibir_matriz(matriz):
#     for linha in matriz:
#         for valor in linha:
#             print(f"{valor:3}", end=" ")
#         print()

# Preencher a matriz com valores aleatórios
# matriz = preencher_matriz()

# Exibir a matriz na tela
# print("Matriz 7x7 com valores aleatórios:")
# exibir_matriz(matriz)

# Encontrar posição do maior e do menor valor e suas contagens
# maior_posicao, contagem_maior, menor_posicao, contagem_menor = encontrar_maior_menor(matriz)

# Exibir informações sobre o maior e o menor valor
# print(f"\nMaior valor: {matriz[maior_posicao[0]][maior_posicao[1]]} (Posição: Linha {maior_posicao[0] + 1}, Coluna {maior_posicao[1] + 1})")
# print(f"Quantidade de vezes que o maior valor aparece: {contagem_maior}")
# print(f"Menor valor: {matriz[menor_posicao[0]][menor_posicao[1]]} (Posição: Linha {menor_posicao[0] + 1}, Coluna {menor_posicao[1] + 1})")
# print(f"Quantidade de vezes que o menor valor aparece: {contagem_menor}")


# Exercício teste do final do Modulo 4.7 Matriz

# matriz = [[1 if i==j else 0 for j in range(5)] for i in range(5)]
# for i in range(5):
#    print(matriz[i])
