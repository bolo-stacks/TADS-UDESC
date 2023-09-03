"""
Flag são variáveis bool, sinalizadores
ela avisa quando falso ou verdadeiro
Nesse exemplo vamos buscar um múltiplo
de 17 entre 100 e 200
Não é necessário a utilização da palavra flag,
pois é somente uma variável bool que chamamos flag
"""


flag = False  # não existe ainda
for i in range(100, 200):
    if i % 17 == 0:
        flag = True  # agora marcamos a flag quando ela encontrar o múltiplo de 17 na condicional.
if flag:  # Quando a flag for True executa esse loop
    print("Encontramos")
else:
    print("Não foi encontrado nenhum múltiplo de 17!")

# Exemplo com a variável flag com outro nome
multiply_17 = False
for i in range(100, 200):
    if i % 17 == 0:
        multiply_17 = True
if multiply_17:
    print("Encontramos")
else:
    print("Não encontramos")
