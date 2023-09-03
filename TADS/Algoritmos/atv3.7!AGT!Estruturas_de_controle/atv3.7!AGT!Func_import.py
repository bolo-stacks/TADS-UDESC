# importa todas # as funções matemáticas
# import math

# importa somente a função específica necessária ao programa
# from math import sqrt (square root)

# importa tudo da biblioteca math
# from math import *

import math
"""
Utilizando as funções:
math.ceil(<expr>) arredonda para cima
math.copysign(x, y) obtém o valor absoluto de x, mas com o sinal de y
math.fabs(<expr>) Valor absoluto da expressão
math.floor(<expr>) arredonda para baixo
math.fmod(x, y) resto da divisão de x por y (float, para inteiro usar %)
math.trunc(<expr>) parte inteira da expressão 
math.exp(x) e**x define expoente
math.log(x) logaritmo natural de x (base e)
math.log(x, y) logaritmo de x na base y (ex.: math.log(1000, 10))
math.pow(x, y)x**y expoente
math.sqrt(x) raiz quadrada de x
"""


import random
'''
random.random() adivinha o que isso faz
x = (random.random() * random.random()) + random.random()
'''

x = random.random()  # gera um número entre 0 e 1
n = int(x * 200 * 1000 / 100)  # utiliza a função random para gerar outros números
print(n)

'''
# gera um número aleatorio entre 1 e 10 inteiro
random.randint(1,10)  
'''

x = random.randint(1, 10)
print(x)
