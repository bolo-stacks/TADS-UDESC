"""

1)
Algoritmo para ler o vetor (lista) de
oito números inteiros e imprimir os
conteúdos do vetor lido (em ordem normal)

a) Altere o algoritmo para imprimir
na ordem inversa.

b) Altere exercício para também mostrar a
soma de seus elementos e apresentar quantos
deles são positivos.

c) Ler dois vetores de 5 posições e calcular
o produto escalar entre ambos.

d) Ler nome e nota de uma turma de até 30 alunos.
Depois exiba uma lista com o nome dos alunos
com nota maior que 7.

e) Preencher com leitura um vetor de 5
posições e informe a posição em que um
valor x (também lido do teclado) está
no vetor. Caso não seja encontrado, deve
imprimir "-1"
produto escalar = um index da lista multiplicado
pelo index de outra lista
Ex.: [1, 2] * [4, 7] = [(1 * 2) + (2 * 7)]

"""
# 1) Minha versão:
# lista = [0] * 8
# for i in range(len(lista)):
#     lista[i] = int(input())
# print(lista)

# versão do professor
# vetor = []
# for i in range(8):
#     vetor.append(int(input()))
# print(vetor)

# a) inverte a ordem no print
# lista_a = [0] * 8
# for i in range(len(lista_a)):
#     lista_a[i] = int(input())
# lista_a.reverse()
# print(lista_a)

# versão do professor
# vetor = []
# for i in range(8):
#     vetor.append(int(input()))
# print(vetor)
# print("Vetor invertido:")
# for i in range(7, -1, -1):
#     print(vetor[i])

# versão 2 do professor
# vetor = []
# for i in range(8):
#     vetor.append(int(input()))
# print(vetor)
# print("Vetor invertido:")
# for i in range(8):
#     print(vetor[-(i + 1)])


# b) apresentar a soma e quantos são positivos
# lista_b = [0] * 8
# for i in range(len(lista_b)):
#     lista_b[i] = int(input())
# print(sum(lista_b))
# for i in range(len(lista_b)):
#     if lista_b[i] >= 0:
#         print(lista_b[i])

# versão do professor
# vetor = []
# for i in range(8):
#     vetor.append(int(input()))
# print("Lista:", vetor)
#
# soma = 0
# n_pos = 0
# positivos = []
# for i in range(8):
#     soma = soma + vetor[i]
#     if vetor[i] >= 0:
#         positivos.append(vetor[i])
#         n_pos = n_pos + 1
# print("Soma dos itens da lista:", soma)
# print("Itens positivos da lista:", positivos)
# print("Número de itens positivos na lista:", n_pos)


# c) Ler dois vetores de 5 posições e calcular
# o produto escalar entre ambos.
# Escalar Ex.: [1, 2] * [4, 7] = [(1 * 2) + (2 * 7)]

# lista_esc1 = []
# lista_esc2 = []
# lista_escalar = []
# for i in range(5):
#     lista_esc1.append(int(input("Item da lista 1:")))
#     lista_esc2.append(int(input("Item da lista 2:")))
#     lista_escalar.append(lista_esc1[i] * lista_esc2[i])
# print("Lista 1:", lista_esc1)
# print("Lista 2:", lista_esc2)
# print("Lista escalar", sum(lista_escalar))

# O algoritmo abaixo está rodando, mas eu fiz errado
# a função escalar

# lista_c = [0] * 5
# vetor_c = 0
# lista_c2 = [0] * 5
# vetor_c2 = 0
# for i in range(len(lista_c)):
#     lista_c[i] = int(input())
#     vetor_c = lista_c[0] * lista_c[1] * lista_c[2] * lista_c[3] * lista_c[4]
# print(lista_c)
# print(vetor_c)
#
# for i in range(len(lista_c2)):
#     lista_c2[i] = int(input())
#     vetor_c2 = lista_c2[0] * lista_c2[1] * lista_c2[2] * lista_c2[3] * lista_c2[4]
# print(lista_c2)
# print(vetor_c2)
# print(vetor_c * vetor_c2)

# d) Ler nome e nota de uma turma de até 30 alunos.
# Depois exiba uma lista com o nome dos alunos
# com nota maior que 7.

# lista_d = [0] # 30 # Nomes
# lista_d2 = [] # Notas
# lista_d7 = [] # Lista das notas acima de 7
# nome = 0
# notas = 0
# for i in range(len(lista_d)):
#     nome = str(input("nome:"))
#     lista_d[i] = nome
#     notas = int(input("nota:"))
#     lista_d2.append(notas)
#     if notas >= 7:
#         lista_d7.append(nome)
#         lista_d7.append(notas)
#
# print(lista_d)
# print(lista_d2)
# print(lista_d7)

# Versão do professor:

# nomes = []
# notas = []
# notas7 = []
#
# for i in range(1):
#     nomes.append(input("Nome:"))
#     notas.append((int(input("Nota:"))))
#     if notas[i] >= 7:
#         notas7.append(nomes[i])
#         notas7.append(notas[i])
#
# print(nomes)
# print(notas)
# print(notas7)

# e) Preencher com leitura um vetor de 5
# posições e informe a posição em que um
# valor x (também lido do teclado) está
# no vetor. Caso não seja encontrado, deve
# imprimir "-1"

# vetor5 = []
# for i in range(2):
#     vetor5.append(int(input()))
# print("Lista:", vetor5)
# xis = (int(input("Busca na lista:")))
# posit = -1
# for i in range(2):
#     if vetor5[i] == xis:
#         posit = i
#         break
# print(xis, "está na posição", posit)
