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
