# Programa para detectar ano bissexto.

ano = int(input('Digite o ano:'))

if ano % 4 == 0:
    print('Ano', ano, 'é bissexto.')
elif ano % 2 == 0:
    print('Ano', ano, "é par.")
else:
    print('Ano', ano, 'é impar.')
