"""
Escrever um algoritmo que leia o nome
de um aluno e as notas das três provas que
ele obteve no semestre.
No final informe o nome do aluno e
a sua média (aritmética).
"""

# Média das notas do aluno

print('Programa que calcula a média das notas do aluno.')  # Interação com o usuário
nom = str(input('Nome do aluno:'))  # Entrada de dados
n1 = float(input('Nota do primeiro mês:'))  # Entrada de dados
n2 = float(input('Nota do segundo mês:'))  # Entrada de dados
n3 = float(input('Nota do terceiro mês:'))  # Entrada de dados
md = (n1 + n2 + n3) / 3  # Fórmula de cálculo da média
print('A média das notas do aluno ', nom, ' é ', md)  # Resposta ao usuário

if md >= 6 and n1 >= 5 and n2 >= 5 and n3 >= 5:
    print('nom, "foi aprovado!')
else:
    print('nom', 'foi reprovado.')
