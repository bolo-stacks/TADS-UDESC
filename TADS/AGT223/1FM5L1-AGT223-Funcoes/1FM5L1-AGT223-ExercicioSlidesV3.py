# algoritmo com menu para calcular a área das seguintes figuras geométricas

'''
ALtere o programa com menu de cálculo de áreas separando cada um dos cálculos em diferentes funções.
retornam a área calculada (ex. area = areacirculo(raio)).
'''

# v3 com funções que recebem o valor diretamente e retornam o resultado do cálculo:


#  definindo a funções:
def area_trapezio(x, y, z):
    a_trap = ((x + y) * z) / 2
    return a_trap


def area_quadrado(x):
    a_quad = x ** 2
    return a_quad


def area_retangulo(x, y):
    a_ret = x * y
    return a_ret


def area_circulo(x):
    pi = 3.14
    a_circ = pi * (x ** 2)
    return a_circ


# Menu do algoritmo:
opcao = ''
while opcao != 'S':

    print('\n\nEscolha uma opção:')
    print('     [T]rapézio')
    print('     [Q]uadrado')
    print("     [R]etângulo")
    print('     [C]írculo')
    print('     [S]air')
    opcao = input(':')
    opcao = opcao.upper()  # Muda pra maiúscula pra reduzir o código.

    # Entrada de dados de cada opção do menu:
    # [0] é porque se o usuário escrever círculo irá ser capturada a primeira letra somente.

    if opcao[0] == 'T':
        x = int(input('Entre com o valor da base 1 do trapézio:'))
        y = int(input('Entre com o valor da base 2 do trapézio:'))
        z = int(input('Entre com o valor da altura do trapézio:'))
        area = area_trapezio(x, y, z)
        print('A área do trapézio é', area)

    elif opcao[0] == 'Q':
        x = int(input('Entre com o valor do lado do quadrado:'))
        area = area_quadrado(x)
        print('A área do quadrado é', area)

    elif opcao[0] == 'R':
        x = int(input('Entre com o valor do comprimento do retângulo:'))
        y = int(input('Entre com o valor da largura do retângulo:'))
        area = area_retangulo(x, y)
        print('A área do retângulo é', area)

    elif opcao[0] == 'C':
        x = int(input('Entre com o valor do raio do círculo:'))
        area = area_circulo(x)
        print('A área do círculo é:', area)

    elif opcao[0] != 'S':
        print('Opção inválida!')
