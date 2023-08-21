"""
Aprendendo loops
"""


# loop 1

def retorna():
    numero = int(input('Digite um número: '))
    print(f'Você digitou o número {numero}')


exec1 = True

while exec1:
    retorna()
    op = str(input('Quer continuar a ler os números por extenso? [S/N] '))
    if op == 'n':
        exec1 = False
        exit('Obrigado por usar nosso programa.')

