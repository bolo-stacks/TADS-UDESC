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

def soma(x, y):
    s = x + y
    return s


x1 = int(input('Entre com o primeiro número para calcular a soma: '))
y1 = int(input('Entre com o segundo número para calcular a soma: '))
x = soma(x1, y1)
print(x)

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
Memória:

Passagem de parâmetros por valor são alterações no valor original da variável, técnica utilizada em python. Isso não é definido explicitamente em python.

Passagem de parâmetros por referência permite que altere o conteúdo das variáveis passadas como parâmetro. Este formato é utilizado em outras linguagens de programação. Alterar a referência altera a variável principal.

Quando criamos um valor primitivo (int, float, bool), o nome da variável define o local na memória do conteúdo.

Com estruturas como strings, list, tuple, set, os nomes das variáveis definem onde essas estruturas estão na memória.

Neste caso, listas, strings, sets tuple, são passadas por referência enquanto que int, float, bool são passadas por valor.

Para fazermos a troca de parâmetros podemos encapsular o valor primitivo em uma list ou set.

Ex.:
'''

# Passagem de parâmetros por -referência-
# Altera a referência para alterar a variável principal
# Troca por parâmetros em python
# Passando uma lista para uma função.
# A variável principal na memória é alterada através de referências que estão em outros endereços na memória.
# listas, conjuntos, strings etc são passagens por referência.

# def altera_lista(lista):
#     lista[0] = 6
#     lista[1] = 7

# lista1 = [1, 2, 3, 4, 5]
# altera_lista(lista1)
# print(lista1)


# Passagem de parâmetros por valor em python -cópia-
# alterar a -cópia- da variável também altera a variável principal
# A cópia refere-se diretamente ao mesmo endereço que o principal na memória.
# int, bool, float etc são passagens por valor.

# lista1 = [1, 2, 3]
# lista2 = lista1
# lista2[1] = 4
# print(lista1)
