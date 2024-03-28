# 5.5 Exercício: Função 2


# Exercício 1:
# Crie uma função que receba dois números e calcule a exponenciação (potência) do primeiro pelo segundo, ou seja, o primeiro número é a base e o segundo é o expoente. Nome da função: potencia().

# v1
# def potencia(base, expoente):
#     resultado = base ** expoente
#     return resultado

# v2
# def potencia(base, expoente):
#     return base**expoente

# v3
# def potencia(base,expoente):
#     # usando repetição
#     resposta = 1
#     for i in range(expoente):
#         resposta *= base
#     return resposta


# Exercício 2:
# Faça uma função troca() que recebe uma lista com dois valores e troca o conteúdo dos dois. Ou seja, o primeiro elemento da lista se transforma no segundo e o segundo se transforma no primeiro.

# v1
# def troca(v):
#     v[0], v[1] = v[1], v[0]

# v2
# def troca(V):
#     aux = V[0]
#     V[0] = V[1]
#     V[1] = aux

# Exercício 3:
# Faça uma função para calcular o fatorial de um número. Receba como parâmetro um número n e retorne como resposta n!
# Obs.: nome da função deve ser fatorial()

# v1
# def fatorial(n):
#     resultado = 1
#     for i in range(2, n + 1):
#         resultado *= i
#     return resultado

# v2
# def fatorial(n):
#     resultado=1
#     num=1
#     while num <= n:
#         resultado *= num
#         num += 1
#     return resultado


# Exercício 4:
# Crie uma função maior() que recebe três valores e retorna o maior dos três.

# v1
# def maior(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# v2
# def maior(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=c:
#         return b
#     return c


# Exercício 5:
# Informe o valor de x no retorno da função minhaFuncao() recebendo como parâmetro os seguintes valores: 1, 2 e 3

# Resposta do valor final de x: 2 (revisar)

# def minhaFuncao(a, b, c):
#     x = a + b * c
#     y = a * b + c
#     return x - y


# print(minhaFuncao(1, 2, 3))
