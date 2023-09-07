"""
Testar a programação das linhas a seguir no
seu editor Python. Fazer um programa para resolver
a radiciação do número 9. Este exercício não é
necessário entregar, basta treinar no Python.
"""

# Exemplo de potenciação

print("base ^ expoente:")
base = int(input("Base: "))
expoente = int(input("Expoente: "))

potencia = 1
count = 1

while count <= expoente:
    potencia *= base  # Potencia = base * base * base .....
    count += 1  # cont = count + 1

print(base, "^", expoente, "=", potencia)
