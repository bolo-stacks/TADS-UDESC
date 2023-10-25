'''
Algoritmo para calcular quantos dias de vida o usuário tem desde o seu nascimento.
'''

# Entrada
dia = int(input("\nNasceu em que dia:"))
mes = int(input("Nasceu em que mês:"))
ano = int(input("Nasceu em que ano:"))

dia_atual = int(input("\nDia atual:"))
mes_atual = int(input("Mês atual:"))
ano_atual = int(input("Ano atual:\n"))

# Função básica de cálculo de dias corridos:


def diascorridos(dia, mes, ano):
    # mês 1, 2,  3,  4,  5,   6,   7,   8,   9,   10,  11,  12
    tabelameses = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    # dias corridos até início do ano.
    dias = int(ano * 365.5)

    # mais os dias até o mês atual.
    dias += tabelameses[mes - 1]

    # Contando ano bissexto
    if mes > 2 and ano % 4 == 0:
        dias += 1

    # mais os dias do mês corrente
    dias += dia
    return dias


# Cálculo em dias:
dias = diascorridos(dia_atual, mes_atual, ano_atual) - \
    diascorridos(dia, mes, ano)

print("\nVocê tem", dias, "\n")
