"""
Escreva um programa que pergunte a distância
que um passageiro deseja percorrer em km.
Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até de 200 km,
e R$ 0,45 para viagens mais longas.
"""


def retorna():
    print('Calculo do valor da passagem de\nacordo com a distância.')
    dist = float(input('Entre com a distância a ser percorrida em quilômetros:'))

    if dist <= 200:
        tot = dist * 0.50
        print('O valor da passagem para %.0f quilômetros é R$%.2f.' % (dist, tot))

    if dist > 200:
        tot = dist * 0.45
        print('O valor da passagem para %.0f quilômetros é R$%.2f.' % (dist, tot))


exec1 = True

while exec1:
    retorna()
    op = str(input('Quer continuar a ler os números por extenso? [S/N] '))
    if op == 'n' or op == 'N':
        exec1 = False
        exit('Obrigado por usar nosso programa.')
