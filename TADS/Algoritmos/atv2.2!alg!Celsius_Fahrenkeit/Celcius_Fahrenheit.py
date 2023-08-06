"""
Ler uma temperatura em graus Celsius e
apresentá-la em graus Fahrenheit.
A formula da conversão F=(9*C+160)/5,
sendo F a temperatura em Fahrenheit e
C a temperatura em graus Celsius.
"""

# Programa que transforma Graus Celsius em Fahrenheit

print("Entre com a temperatura em Celsius a ser convertida em Fahrenheit")  # Interação com o usuário
cel = float(input('Temperatura em Celsius:'))                               # Entrada de dados
fah = float((9 * cel + 160) / 5)                                            # Fórmula
print('Sua temperatura convertida em Fahrenheit é de ', fah, 'ºF')          # Resposta ao usuário
