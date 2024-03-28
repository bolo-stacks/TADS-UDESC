"""
Calcula o valor da exponenciação de 
um número inserido pelo usuário.
"""

bas = int(input("\nInsira a base da exponenciação: "))
exp = int(input("\nInsira o expoente: "))
res = bas ** exp
print("\nO resultado de %d elevado na %d é %d" % (bas, exp, res))
