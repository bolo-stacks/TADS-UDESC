"""
Faça um algoritmo para ler um número indeterminado de dados, 
contendo cada um, a idade de um indivíduo. O último dado, 
que não entrará nos cálculos, contém o valor de idade negativa. 
Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. 
A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
Ex:
Entrada: 34, 56, 44, 23, -2
Saída: 39,25
"""
idade_lista = []
idade = 1
while idade >= 0:
    idade = int(input())
    if idade >= 0:
        idade_lista.append(idade)

media = sum(idade_lista) / len(idade_lista)
print("%.2f" % media)
