"""
Algoritmo para executar a sequencia
fibonacci de um número do usuário.
"""

fibo_user = int(input("Entre com um número para exibir a sequencia fibonacci:"))
fibo_item_0 = 0
fibo_item_1 = 1
fibo_list = [fibo_item_0, fibo_item_1]
fibo_item = 0

for i in range(1, fibo_user - 1):
    fibo_item_n = fibo_item_0 + fibo_item_1
    fibo_list.append(fibo_item_n)
    fibo_item_0 = fibo_item_1
    fibo_item_1 = fibo_item_n
print(fibo_list)
