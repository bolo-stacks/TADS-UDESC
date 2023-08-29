"""
Calcular a média das notas de uma turma. 
Entrada do programa: o número de alunos 
da turma e na sequência as notas de cada um dos alunos. 
A média deve ser mostrada com uma casa decimal.
"""

num = int(input('Número de alunos:'))
x = 1

for i in range(0, num):
    nota = float(input('Entre com a nota do aluno %f' % x))
    x = x + 1

