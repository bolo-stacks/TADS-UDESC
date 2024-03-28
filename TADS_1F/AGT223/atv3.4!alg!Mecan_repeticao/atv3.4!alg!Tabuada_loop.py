"""
Tabuada de multiplicação do número
inserido pelo usuário
ex: 1 * 1 = 1, 1 * 2 = 2, 1 * 3 = 3...
"""

num = int(input('Qual o número:'))
i = 0
print('\nTabuada do', num)
for i in range(11):
    print('%2d x %2d = %2d' % (num, i, num * i))

# Tabuada de todos os números.

cont = str(input('Deseja ver a tabuada completa? (s/n)'))
if cont == "s":
    for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        print('\nTabuada do', n)
        for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            print('%2d x %2d = %2d' % (n, i, n * i))
