"""                                                                     # comentário
Esse programa permite trocar o valor das
variáveis 
"""

print('Programa que inverte o valor das variáveis A e B')  # imprime na tela
a = int(input("Entre com o valor de A: "))  # entrada de dados para a variável A
b = int(input("Entre com o valor de B: "))  # entrada de dados para a variável B
print("O valor de A é ", a, " e o valor de B é ", b)  # mostra na tela os valores definidos pelo
(a, b) = (b, a)  # fórmula para troca dos valores das variáveis
print("O novo valor de A é ", a, " e o novo valor de B é ", b)  # mostra na tela o novo valor trocado

# alterando programa teste
