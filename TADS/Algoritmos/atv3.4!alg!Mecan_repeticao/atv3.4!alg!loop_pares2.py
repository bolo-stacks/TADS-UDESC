"""
Loop condicional WHILE
Começa o segundo exercício que conta os
números pares entre dois números do usuário
"""

# Mostra quantos números pares tem no range do loop

num1 = int(input('Entre com o menor número:'))  # variável do loop
num2 = int(input('Entre com o maior número:'))  # variável da contagem
i = num1
par = 0
while i <= num2:
    if i % 2 == 0:
        par = par + 1
    i = i + 1
print('São', par, 'números pares de', num1, 'a', num2)
