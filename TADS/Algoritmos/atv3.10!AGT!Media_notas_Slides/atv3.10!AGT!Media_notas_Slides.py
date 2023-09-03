"""
Algoritmo que leia três notas de um aluno e 
imprima a mensagem de aluno aprovado ou reprovado conforme:
média final maior ou igual a 6 e nenhuma
das notas for inferior a 5 o aluno foi aprovado,
caso contrário foi reprovado.
"""

nota_1 = float(input("Primeira nota:"))
nota_2 = float(input("Segunda nota:"))
nota_3 = float(input("Terceira nota:"))
media = (nota_1 + nota_2 + nota_3) / 3
if nota_1 >= 5 and nota_2 >= 5 and nota_3 >= 5 and media >=6:
    print("Aprovado")
else:
    print("Reprovado")
