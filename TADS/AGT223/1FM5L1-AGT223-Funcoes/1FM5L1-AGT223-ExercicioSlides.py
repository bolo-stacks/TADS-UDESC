# algoritmo com menu para calcular a área das seguintes figuras geométricas
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

    # [0] é porque se o usuário escrever círculo irá ser capturada a primeira letra somente.
    if opcao[0] == 'T':
        b1_trap = int(input('Entre com o valor da base 1 do trapézio:'))
        b2_trap = int(input('Entre com o valor da base 2 do trapézio:'))
        h_trap = int(input('Entre com o valor da altura do trapézio:'))

        # calcula arranjo: A = ((b1+b2) * h) / 2
        a_trap = ((b1_trap + b2_trap) * h_trap) / 2
        print('A área do trapézio é', a_trap)

    elif opcao[0] == 'Q':
        l1_quad = int(input('Entre com o valor do lado do quadrado:'))

        # Calcula combinação: A = l1 ** 2
        a_quad = l1_quad ** 2
        print('A área do quadrado é', a_quad)

    elif opcao[0] == 'R':
        c_ret = int(input('Entre com o valor do comprimento do retângulo:'))
        l_ret = int(input('Entre com o valor da largura do retângulo:'))

        # Calcula combinação: a = c * l
        a_ret = c_ret * l_ret
        print('A área do retângulo é', a_ret)

    elif opcao[0] == 'C':
        r_circ = int(input('Entre com o valor do raio do círculo:'))

        # Calcula combinação: a = pi * (r ** 2)
        pi = 3.14
        a_circ = pi * (r_circ ** 2)
        print('A área do círculo é:', a_circ)

    elif opcao[0] != 'S':
        print('Opção inválida!')
