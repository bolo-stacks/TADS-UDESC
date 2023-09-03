"""
Menu em match - case
"""

print("Escolha entre [T]riangulo, [Q]uadrado, [R]etangulo")

op = input()

match op:
    case "T":
        print('Triangulo')
    case "Q":
        print("Quadrado")
    case "R":
        print("Retângulo")
    case default:
        print("Inválido")
