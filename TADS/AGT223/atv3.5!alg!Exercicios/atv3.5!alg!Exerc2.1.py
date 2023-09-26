# Entrada do programa: o número de alunos da turma e na sequência as notas de cada um dos alunos

n = int(input("Digite o número de alunos da turma: "))  # Lê o número de alunos
notas = []  # Cria uma lista vazia para armazenar as notas
soma = 0  # Cria uma variável para armazenar a soma das notas

for i in range(n):  # Repete n vezes
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))  # Lê a nota do aluno i+1
    notas.append(nota)  # Adiciona a nota à lista de notas
    soma += nota  # Adiciona a nota à soma das notas

media = soma / n  # Calcula a média das notas
print(f"A média da turma é {media:.1f}")  # Imprime a média da turma com duas casas decimais
