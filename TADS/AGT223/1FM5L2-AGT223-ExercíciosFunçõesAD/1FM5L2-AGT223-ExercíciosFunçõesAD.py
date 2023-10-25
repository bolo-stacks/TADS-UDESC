'''
Exercícios AD do Módulo 5, funções:
'''


# Exercício 1:
# Crie a função soma(a,b) que recebe dois valores, soma eles e retornar o resultado. O nome da função deve ser "soma" (sem aspas e todas as letras minúsculas).

# v1
# def soma(x, y):
#     s = x + y
#     return s

# v2

# def soma(a,b):
#     return a+b


# Exercício 2:
# Desenvolva uma função somatório(n) para calcular a soma de todos os valores ímpares de 1 até o número indicado. Ex. somatório(10) deve retornar 25 (1+3+5+7+9).

# v1

# def somatorio(n):
#     soma = 0
#     for i in range(1, n + 1, 2):
#         soma += i
#     return soma

# v2

# def somatorio(n):
#     if n <= 1: return 1
#     soma = 0
#     for i in range(1,n+1):
#         if i%2!=0:
#             soma += i
#     return soma


# Exercício 3:
# Desenvolva uma função sequencia(n) para calcular a sequência da potência de 2 até o valor informado.

# v1

# def sequencia(n):
#     p = 2
#     while p <= n:
#         print(p)
#         p *= 2


# v2

# def sequencia(n):
#     v = 2
#     while v<=n:
#         print(v)
#         v = v+v


# Exercício 4:
# Faça uma função chamada múltiplos7(inicio,fim) que retorna a SOMA dos múltiplos de 7 entre um valor inicial e um valor final (inclusive).

# def multiplos7(inicio, fim):
#     s = 0
#     for n in range(inicio, fim + 1):
#         if n % 7 == 0:
#             s += n
#     return s


# Exercício 5:
# Qual a saída da função minhaFuncao() abaixo?

# Resposta: -77846 (Revisar se não houve alterações no exercício.)

# def minhaFuncao(a, b, c):
#     x = a + b * c
#     y = a * b + c
#     return x-y
#     x = y * 2


# lista = [3, 5, 7]
# k = minhaFuncao(lista[0], lista[1], lista[2])
# lista = [6, 4, k-77872]
# print(lista[0] + lista[1] + lista[2])
