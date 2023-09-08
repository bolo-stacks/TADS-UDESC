
"""
Fazer o mdc dos números do usuário utilizando a biblioteca
numpy e os atributos gcd (mdc) e reduce.
Entre com os números separados por espaço e tecle enter ao final.
"""

##################
# Versão melhorada

import numpy as np

numbers = list(map(int, input().split()))  # lê os números separados por espaço e coloca em uma lista
result = np.gcd.reduce(numbers)  # aplica a função lcm para todos os números da lista
print(result)  # imprime o resultado
