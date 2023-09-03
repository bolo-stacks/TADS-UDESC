"""
Não tem como um menu ser mais básico que isso
"""

print("MENU")
print("\n[R]etangulo")
print("\n[L]osangulo")
print('\n[C]irculo')

op = input()
if op == "R" or "t":
    print("Você escolheu retângulo")
elif op == "L" or "l":
    print("Você escolheu losangulo")
elif op == "C" or "c":
    print("Você escolheu círculo")
else:
    print("Opção inválida")
