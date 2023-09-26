"""
Calcular a média das notas de uma turma.
Entrada do programa: o número de alunos
da turma e na sequência as notas de cada um dos alunos.
A média deve ser mostrada com uma casa decimal.
"""


n = int(input())
notas = []
soma = 0

for i in range(n):
    nota = float(input())
    notas.append(nota)
    soma += nota

media = soma / n
print('%.1f' % media)

'''
Trecho de Código: Média de notas usando for (Python)
# número de alunos na turma
'''
n = int(input())

# calcula a média - soma todos os valores e divide por n
soma = 0
for linha in range(0, n):
    nota = float(input())
    soma = soma + nota
media = soma / float(n)

# exibe a média
print('%.1f' % media)

'''
Trecho de Código: Média de notas usando while (Python)
# número de alunos na turma
'''

n = int(input())

# calcula a média - soma todos os valores e divide por n
soma = 0
cont = 0
while cont < n:
    nota = float(input())
    soma = soma + nota
    cont = cont + 1
media = soma / float(n)

# exibe a média
print('%.1f' % media)