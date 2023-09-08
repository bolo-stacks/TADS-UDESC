"""
PROBLEMA
Uma associação beneficente vai criar caixas de lanches
para distribuir. Cada caixa deve ter 1 suco, 1 biscoito
e 1 chocolate.

No mercado foram encontrados na seguinte quantidade:
- suco, embalagem com 15 unidades.
- biscoito, embalagem com 20 unidades.
- chocolate, embalagem com 25 unidades.

Perguntas:
a) Quantas caixas de lanches deverão ser montadas de
tal forma que não reste nenhum produto.
b) Quantas embalagens de suco, biscoito e chocolate
deverão ser compradas.

Solução:

a) mmc(15, 20, 25)
b) mmc / número de unidades de cada ítem (15, 20 e 25)
"""

##################
# Versão melhorada

import numpy as np

numbers = (15, 20, 25)  # lê os números separados por espaço e coloca em uma lista
result = np.lcm.reduce(numbers)  # aplica a função lcm para todos os números da lista
print("Resposta da A) mmc de 15, 20 e 25 é %d" % result)  # imprime o resultado
print("Resposta da B) quantas devem ser compradas é\n",
      (int(result / 15)), "embalagens de suco\n",
      (int(result / 20)), "embalagens de biscoito\n",
      (int(result / 25)), "embalagens de chocolate")
