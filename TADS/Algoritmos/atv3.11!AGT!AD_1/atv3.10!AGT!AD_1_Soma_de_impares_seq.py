"""
Soma de Ímpares Consecutivos II

Leia um valor inteiro N que é a quantidade de casos de 
teste que segue. Cada caso de teste consiste em 
dois inteiros X e Y. Você deve apresentar a soma de todos 
os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a 
quantidade de casos de teste que segue. 
Cada caso de teste consiste em uma linha contendo 
dois inteiros X e Y.

Saída
Imprima a soma de todos os valores ímpares entre X e Y.

Entrada:
7
4 e 5
13 e 10
6 e 4
3 e 3
3 e 5
3 e 4
3 e 8

Saída:
-
0
11
5
0
0
0
12
"""

lista = []
lista_impar = []
qnt = int(input())

for i in range(0, qnt):
    num_1 = int(input())
    num_2 = int(input())
    if num_1 <= num_2:
        lista.append(num_1)
        lista.append(num_2)
    else:
        lista.append(num_2)
        lista.append(num_1)
    x = min(lista)
    while x < max(lista):
        x = x + 1
        if x % 2 > 0:
            lista_impar.append(x)

    if len(lista_impar) < 2:
        print("\n0")
    else:
        sm_impar = sum(lista_impar)
        print("\n", sm_impar)
    list.clear(lista)
    list.clear(lista_impar)
