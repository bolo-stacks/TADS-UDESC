"""
Programa encontra os múltiplos de 37
acima de 200 até 10000
utilização do while true break continue
"""

num = 200
while num < 10000:
    num = num + 1
    if num % 37 == 0:
        print('Encontrei', num, "múltiplos de 37")
        n = 20000

'''
Versão Elegante com while true break
'''

nim = 200
while True:
    nim = nim + 1
    if nim % 37 == 0:
        print('Encontrei', nim, "múltiplos de 37 com o while true break")
        break  # Finaliza o laço if

'''
Utilização do continue
Programa procura todos os múltiplos de 
quatro menores que 30 e imprime os que
não são múltiplos de quatro
'''

nunmiru = 0
while nunmiru < 30:
    nunmiru = nunmiru + 1
    if nunmiru % 3 == 0:
        continue  # Volta pro while se nom for divisível por 4
    print(nunmiru)
