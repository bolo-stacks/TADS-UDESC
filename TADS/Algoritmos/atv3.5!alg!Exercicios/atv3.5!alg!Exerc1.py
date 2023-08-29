"""
Ler um número inteiro e imprimir a seguinte estrutura:

*
**
***
****
*****
******

Obs.: o usuário entra com um valor que é a altura da 
estrutura (número de linhas) e a cada linha, 
são exibidos tantos asteriscos quanto o número da linha. 
Para desenhar três asteriscos, use: print('*'*3)
"""

num = int(input('Entre com um número:'))
x = 1
while x <= num:
    print("*" * x)
    x = x + 1
