"""
Fazer o mmc dos números do usuário utilizando a biblioteca 
numpy e os atributos lcm (mmc) e reduce.
Entre com os números separados por espaço e tecle enter ao final.
"""
# import da minha versão
import numpy as np

# Versão da IA do bing

# import do bing
from math import gcd
from functools import reduce


def lcm(a, b):
    gc = gcd(a, b)  # mdc de dois números
    lc = (a * b) // gc
    return lc


numbers = list(map(int, input().split()))  # lê os números separados por espaço e coloca em uma lista
result = reduce(lcm, numbers)  # aplica a função lcm para todos os números da lista
print(result)  # imprime o resultado

##################
# Versão melhorada

# import numpy as np

numbers = list(map(int, input().split()))  # lê os números separados por espaço e coloca em uma lista
result = np.lcm.reduce(numbers)  # aplica a função lcm para todos os números da lista
print(result)  # imprime o resultado
