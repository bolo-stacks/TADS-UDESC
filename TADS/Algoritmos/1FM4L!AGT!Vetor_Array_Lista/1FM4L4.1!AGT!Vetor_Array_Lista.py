"""
Exemplos de Vetor Array e List
"""

# primeiro exemplo: sem utilizar list
n = int(input("Quantas notas para calcular:"))
media = 0

for i in range(n):
    media = media + float(input())
media = media / n
print(media)

# usando list: 1 forma
notas = [8.0, 5, 2]
tam = len(notas)
for i in range(tam):
    print("\n", notas[i])

# usando list: 2 forma
notas = [8.0, 5, 2]
for i in notas:
    print("\n", i)

# usando list: exemplo de adição à lista
lista = [1, 2, 3, 4]
print("\n", lista)
lista = lista + [5, 6]
print("\n", lista)
lista = lista + [4, 5, 6]
print("\n", lista)

# usando list: multiplicando a lista
lista2 = [1, 2, 3, 4]
print("\n", lista)
lista2 = lista2 * 3
print("\n", lista2)

# usando list: multiplicando a lista para economizar append
tamanho = 10
lista3 = [0] * tamanho
print("\n", lista3)

# lista com tamanh pré-definido pelo usuário
tamanho2 = int(input("\nDigite o tamanho da lista:"))
lista4 = [0] * tamanho2
for i in range(tamanho2):  # for i in range(len(lista4)
    lista4[i] = i + 1
print(lista4)
