"""
Fazer o mmc dos números do usuário utilizando a biblioteca 
numpy e os atributos lcm (mmc) e reduce.
"""

import numpy as np

user_mmc = 1
mmc_list = []
print("Entre com os valores para calcular o mmc,\nquando não quiser mais incluir valores entre com zero (0).")

while user_mmc != 0:
    user_mmc = int(input('\nEntre com o valor para fazer\no mmc (mínimo múltiplo comum):'))
    mmc_list.append(user_mmc)

mmc_list = str(mmc_list)
print(eval(mmc_list))
# a = np.array(mmc_list)
# print(np.lcm([a]))
