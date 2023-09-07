"""
Testar a programação das linhas a
seguir no seu editor Python. Sugestão,
alterar os valores e executar novamente.
Logo depois alterar os valores para
calcular o de MMC(20,7). Este exercício
não é necessário entregar, basta treinar
no Python.
"""


######################################

def mmc(xi, yp):
    if xi > yp:
        z = xi
    else:
        z = yp
    while True:
        if (z % xi == 0) and (z % yp == 0):
            re = z
            break
        z += 1
    return re


#####################################

xis = int(input("Entre com o primeiro número:"))
yps = int(input("Entre com o segundo número:"))
# x=5
# y=10
res = mmc(xis, yps)

print("Minimo Múltiplo Comum de:")
print("x=%d" % xis)
print("y=%d" % yps)
print("Resultado=%d" % res)
