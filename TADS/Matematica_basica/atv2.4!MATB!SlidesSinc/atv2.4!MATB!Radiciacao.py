"""
Entre com o radicando e o índice pra calcular
o radical.

Os elementos de uma radiciação são:

O radicando, número dentro do símbolo da raiz.
O índice, o número que indica o tipo de raiz que se quer calcular.
A raiz, que é o resultado da operação.
"""

rad = int(input("\nEntre com um radicando: "))
ind = int(input("\nEntre com o índice: "))

raiz = (rad ** (1 / ind))
print(f'\nA raiz de {rad} com índice {ind} é {raiz}\n')
