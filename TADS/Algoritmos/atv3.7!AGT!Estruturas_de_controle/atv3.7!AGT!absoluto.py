"""
O comando abs retorna o número absoluto de uma variável.
exemplo: o valor absoluto de -10 é 10.
"""

var = -444
var2 = abs(var)
print(var2)


'''
O comando eval é utilizando para detectar o tipo da variável, se é float, integer
e também faz calculos
'''

xis = (eval(input('Entre com um número:')))
de = "print(xis + 3.5432 * 332)"
eval(de)

# mais um exemplo de eval
a = - 5
b = '12.35'
b = eval(b)
print(a + b)
