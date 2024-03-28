"""
Escreva um programa que pergunte o salário do
funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00,
calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%
"""

print('Esse programa calcula o aumento de seu salário.')
print('Salários abaixo ou iguais à R$ 1.250,00 têm aumento de 15%,\nacima desse valor têm aumento de 10%.')

sal = float(input('Entre com o valor do seu salário:'))

if sal <= 1250:
    sal = ((sal * 15) / 100) + sal
    print('O valor do seu salário com aumento de 15%% é R$ %.2f' % sal)

if sal > 1250:
    sal = ((sal * 10) / 100) + sal
    print('O valor do seu salário com aumento de 10%% é R$ %.2f' % sal)
