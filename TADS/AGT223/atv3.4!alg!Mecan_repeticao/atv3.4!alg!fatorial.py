# Calcular o fatorial do número do usuário

# Fórmula n! = 1 * 2 * 3 * 4 * 5 * ... * n
# Exemplo: 4! = 1 * 2 * 3 * 4 = 24

num = int(input('Entre com o número para calcular o fatorial:'))
i = 1
fatorial = 1
while i <= num:
    fatorial = fatorial * i
    i = i + 1
print('O fatorial de:', num, "é", fatorial)

# Calcular o fatorial do número do usuário
# mesmo programa utilizando for

num = int(input('Entre com o número para calcular o fatorial:'))
fatorial = 1
for i in range(1, num + 1):
    fatorial = fatorial * i
    i = i + 1
print('O fatorial de:', num, "é", fatorial)

