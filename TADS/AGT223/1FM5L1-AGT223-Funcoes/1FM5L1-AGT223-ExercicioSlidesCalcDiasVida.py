'''
Algoritmo para calcular quantos dias de vida o usuário tem desde o seu nascimento.
'''

# Entrada
dia = int(input("Nasceu em que dia:"))
mes = int(input("Nasceu em que mês:"))
ano = int(input("Nasceu em que ano:"))

dia_atual = int(input("Dia atual:"))
mes_atual = int(input("Mês atual:"))
ano_atual = int(input("Ano atual:"))


# Função básica de cálculo de dias corridos:
def diascorridos(dia, mes, ano):
    dias = int(ano * 365.5)


# Cálculo em dias:
dias = diascorridos(dia_atual, mes_atual, ano_atual) - \
    diascorridos(dia, mes, ano)

print(dias)
