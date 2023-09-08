"""
Uma associação comunitária recebeu 18 bolas 
e 12 petecas para doar às crianças.

Quantos kits poderão ser formados com a mesma
quantidade de bolas e petecas.

Solução: mdc de 18 e 12
depois divide os ítens pelo mdc que o
resultado é o número de bolas e petecas
em cada kit.
"""

##################
# Versão melhorada

import numpy as np

numbers = (18, 12)  # lê os números separados por espaço e coloca em uma lista
result = np.gcd.reduce(numbers)  # aplica a função lcm para todos os números da lista
print("O MDC entre 18 e 12 é", result)  # imprime o resultado
print("O número de bolas em cada kit é", (18 / result),
      "\nO número de petecas em cada kit é", (12 / result))

'''
Uma loja de artesanato vai distribuir kits
de amostras, têm 120 pares de brincos,
200 colares e 400 pulseiras.

Quantos kits podem ser formados com quantidade
igual em cada kit.

Solução:
MDC 120, 200, 400
'''

num = (120, 200, 400)
res = np.gcd.reduce(num)
print("\nA quantidades de kits que podem ser formados"
      "\né o MDC entre 120, 200, 400 que é", res)
