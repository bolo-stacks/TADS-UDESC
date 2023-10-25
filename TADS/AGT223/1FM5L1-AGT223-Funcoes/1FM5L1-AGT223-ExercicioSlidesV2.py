# algoritmo com menu para calcular a área das seguintes figuras geométricas
# v2 com funções:


#  definindo a funções:
def area_trapezio():
    x = int(input('Entre com o valor da base 1 do trapézio:'))
    y = int(input('Entre com o valor da base 2 do trapézio:'))
    z = int(input('Entre com o valor da altura do trapézio:'))
    a_trap = ((x + y) * z) / 2
    print('A área do trapézio é', a_trap)


def area_quadrado():
    x = int(input('Entre com o valor do lado do quadrado:'))
    a_quad = x ** 2
    print('A área do quadrado é', a_quad)


def area_retangulo():
    x = int(input('Entre com o valor do comprimento do retângulo:'))
    y = int(input('Entre com o valor da largura do retângulo:'))
    a_ret = x * y
    print('A área do retângulo é', a_ret)


def area_circulo():
    x = int(input('Entre com o valor do raio do círculo:'))
    pi = 3.14
    a_circ = pi * (x ** 2)
    print('A área do círculo é:', a_circ)


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
        area_trapezio()

    elif opcao[0] == 'Q':
        area_quadrado()

    elif opcao[0] == 'R':
        area_retangulo()

    elif opcao[0] == 'C':
        area_circulo()

    elif opcao[0] != 'S':
        print('Opção inválida!')
