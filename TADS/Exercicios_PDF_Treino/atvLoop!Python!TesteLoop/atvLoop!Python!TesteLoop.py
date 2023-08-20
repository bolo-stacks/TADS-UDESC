num_por_extenso = [
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
    'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']


def retorna_numero_por_extenso():
    numero = int(input('Digite um número: '))
    numero_extenso = num_por_extenso[numero]
    print(f'Você digitou o número {numero_extenso}')


exec1 = True

while exec1:
    retorna_numero_por_extenso()
    op = str(input('Quer continuar a ler os números por extenso? [S/N] ')).upper().strip()
    if op == 'N':
        exec1 = False
        exit('Obrigado por usar nosso programa.')
