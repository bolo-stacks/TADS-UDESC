# criar uma função que calcule fatorial.
# Fatorial de 3! é 1 * 2 * 3 = 6

#
# versão primária:
#

# def fatorial(num):
#     fat = 1
#     for i in range(1, num+1):
#         fat *= i
#     return fat

# x = int(input('Entre com um número para calcular o fatorial: '))
# x = fatorial(x)
# print(x, '!')

#
# versão melhorada:
#

# def fatorial(num):
#     if num < 0: return 0
#     if num <= 1: return 1
#     fat = 1
#     for i in range(1, num+1):
#         fat *= i
#     return fat

# x = int(input('Entre com um número para calcular o fatorial: '))
# x = fatorial(x)
# print(x, '!')

#
# Função de soma:
#

# def soma(x, y):
#     s = x + y
#     return s


# x1 = int(input('Entre com o primeiro número para calcular a soma: '))
# y1 = int(input('Entre com o segundo número para calcular a soma: '))
# x = soma(x1, y1)
# print(x)

#
# versão melhorada de soma:
#

# def soma(x, y):
#     return x + y


# x1 = int(input('Entre com o primeiro número para calcular a soma: '))
# y1 = int(input('Entre com o segundo número para calcular a soma: '))
# x = soma(x1, y1)
# print(x)

#
# Função deve vir antes da chamada, exceto se a chamada está dentro de uma função:
#

# def main():
#     x = int(input('Entre com um valor:'))
#     y = int(input('Entre com outro valor:'))
#     s = soma(x, y)
#     print(x, '+', y, '=', s)

# def soma(a, b):
#     return a + b

# main()

#
# Função sem return á chamada de procedimento:
#
# def imprime_soma(a, b):
#     print(a, '+', b, '=', a+b)

# z = int(input('Entre com o primeiro número para somar:'))
# k = int(input('Entre com o segundo número para somar:'))
# imprime_soma(z, k)

'''
Passagem de parâmetros por valor são cópias do valor original da variável, técnica utilizada em python. Isso não é definido explicitamente em python.

Passagem de parâmetros por referência permite que altere o conteúdo das variáveis passadas como parâmetro. Este formato é utilizado em outras linguagens de programação.

Quando criamos um valor primitivo (int, float, bool), o nome da variável define o local na memória do conteúdo.

Com estruturas como strings, list, tuple, set, os nomes das variáveis definem onde essas estruturas estão na memória.

Neste caso, listas, strings, sets tuple, são passadas por referência enquanto que int, float, bool são passadas por valor.

Para fazermos a troca de parâmetros podemos encapsular o valor primitivo em uma list ou set.

Ex.:
'''

# Passando uma lista para uma função.

# def altera_lista(lista):
#     lista[0] = 6
#     lista[1] = 7

# lista1 = [1, 2, 3, 4, 5]
# altera_lista(lista1)
# print(lista1)
