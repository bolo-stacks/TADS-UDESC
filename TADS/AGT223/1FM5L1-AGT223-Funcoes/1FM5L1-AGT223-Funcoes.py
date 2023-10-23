# menu
opcao = ''
while opcao != 's' and opcao != 'S':
    print('\n\nEscolha uma opção:')
    print("     [A]rranjo")
    print('     [C]ombinação')
    print('     [S]air')
    opcao = input(':')

    if opcao == 'a' or opcao == 'A':
        n = int(input('Entre com o valor de n:'))
        r = int(input('Entre com o valor de r:'))
        # calcula arranjo: A = n! / (n-r)!
        nfat = 1
        for i in range(1, n+1):
            nfat *= i

        nr = n - r
        nrfat = 1
        for i in range(1, nr+1):
            nrfat *= i

        a = nfat / nrfat
        print(f'Arranjo ({n},{r}) = {a}')

    elif opcao == 'c' or opcao == 'C':
        n = int(input('Entre com o valor de n:'))
        r = int(input('Entre com o valor de r:'))
        # Calcula combinação: C = n! / (r! * (n-r)!)
        nfat = 1
        for i in range(1, n+1):
            nfat *= i
        rfat = 1
        for i in range(1, r+1):
            rfat *= i

        nr = n - r
        nrfat = 1
        for i in range(1, nr+1):
            nrfat *= i

        c = nfat / (rfat * nrfat)
        print(f'Combinação ({n},{r}) = {c}')

    elif opcao != 's' and opcao != 'S':
        print('Opção inválida!')
