"""
Os termos de Fibonacci são sempre iguais à soma dos dois 
termos anteriores a eles na sequência, e os dois primeiros termos são 1. 
Ou seja:

1, 1, 2, 3, 5, 8, 13, 21, 34...

Porém, não estamos interessados em achar os termos da sequência de Fibonacci, 
mas sim os termos da sequência de Fibonot!

A sequência de Fibonot é composta pelos números que não pertencem à sequência de Fibonacci. 
Mais especificamente, os números inteiros positivos não-nulos. Em ordem crescente!
Eis os primeiros termos de Fibonot:

4, 6, 7, 9, 10, 11, 12, 14, 15...

Sua tarefa é achar o K-ésimo número de Fibonot.
"""

# Variável que escolhe quantos valores fibonacci serão apresentados.
fib_user = 9 - 2  # Diminui dois porque o contador começa no 3 item

# Definem os dois primeiros itens da sequencia fibonacci.
fib1 = 1
fib2 = 1

# Variável contadora a partir do terceiro número da sequencia fibonacci.
fibs = 1

# Variável do loop.
contador_loop_1 = 1

# Define os dois primeiros itens da lista fibonacci.
fibs_lista = [fib1, fib2]

# Loop que adiciona itens na sequencia fibonacci até o ítem determinado pela entrada (ene).
while contador_loop_1 <= fib_user:
    fibs = fib1 + fib2
    fibs_lista.append(fibs)
    fib1 = fib2
    fib2 = fibs
    contador_loop_1 = contador_loop_1 + 1

print(fibs_lista)


# Início do programa que faz uma lista dos ítens que não estão na sequência fibonacci do usuário.
# Contador de loop.

# contador da lista notfibo.
item_da_lista_notfibo = 1

# Lista notfibo, guarda ítens que não estão na lista fibonacci do usuário.
notfibs_lista = []

# Loop notfibo
while (len(notfibs_lista)) < (len(fibs_lista)):

    while item_da_lista_notfibo in fibs_lista:
        item_da_lista_notfibo = item_da_lista_notfibo + 1


    notfibs_lista.append(item_da_lista_notfibo)
    item_da_lista_notfibo = item_da_lista_notfibo + 1
    n = n + 1

print(notfibs_lista)
