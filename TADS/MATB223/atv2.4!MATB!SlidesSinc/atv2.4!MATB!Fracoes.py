"""
Fazer o cálculo das frações do usuário utilizando a biblioteca
numpy e os atributos fractions e list.
Entre com os números separados por espaço e tecle enter ao final.
Efetua as operações matemáticas nas frações inseridas pelo usuário.
Formato de Entrada: 3/4, 2/3, ..., Enter
"""

##################


from fractions import Fraction  # Importa a biblioteca fractions

# Instruções ao usuário

print("\nInsira as frações neste formato 1/3, 2/4, ... Enter\n"
      "separadas por vírgula.\n")

# Loop de entrada do usuário

fractions = []  # cria uma lista vazia
line = input("\nDigite as frações separadas por vírgula:\n")  # lê a linha de entrada
values = line.split(",")  # separa os valores por vírgula
for value in values:  # loop sobre os valores
    fraction = Fraction(value)  # converte o valor em fração
    fractions.append(fraction)  # adiciona a fração na lista
print(fractions)  # imprime a lista


# função de subtração da lista
def sub(lst):  # define uma função chamada subtract que recebe uma lista como argumento
    result = lst[0]  # inicializa o resultado com o primeiro elemento da lista
    for number in lst[1:]:  # itera sobre os elementos restantes da lista
        result -= number  # subtrai cada elemento do resultado
    return result  # retorna o resultado


# Função para multiplicação

def mult(items):  # define uma função chamada multiply_list que recebe uma lista como argumento
    total = 1  # inicializa o total com 1
    for item in items:  # itera sobre os itens da lista
        total *= item  # multiplica cada item pelo total
    return total  # retorna o total


# Função para divisão das frações.

def div(items):  # define uma função chamada multiply_list que recebe uma lista como argumento
    total = items[0]
    for item in items[1:]:  # itera sobre os itens da lista
        total /= item  # multiplica cada item pelo total
    return total  # retorna o total

# "print" dos resultados das operações feitas
# com os valores inseridos pelo usuário


print("A Soma das frações é", (sum(fractions)))  # imprime a soma
print("A Subtração das frações é", (sub(fractions)))
print("A Multiplicação das frações é", (mult(fractions)))
print("A divisão das frações é", (div(fractions)))
