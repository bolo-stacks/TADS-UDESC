"""
Rosy é uma talentosa professora do Ensino Médio
que já ganhou muitos prêmios pela qualidade de
sua aula. Seu reconhecimento foi tamanho que foi
convidada a dar aulas em uma escola da Inglaterra.
Mesmo falando bem inglês, Rosy ficou um pouco
apreensiva com a responsabilidade, mas resolveu
aceitar a proposta e encará-la como um bom desafio.

Tudo ocorreu bem para Rosy até o dia da prova.
Acostumada a dar notas de 0 (zero) a 100 (cem),
ela fez o mesmo na primeira prova dos alunos da
Inglaterra. No entanto, os alunos acharam estranho,
pois na Inglaterra o sistema de notas é diferente:
as notas devem ser dadas como conceitos de A até E.
O conceito A é o mais alto, enquanto o conceito E é
o mais baixo.

Nota 0 = E
Nota 1 a 35 = D
Nota 36 a 60 = C
Nota 61 a 85 = B
Nota 86 a 100 = A

Entrada: N (0 ≤ N ≤ 100)
Saída: (A, B, C, D, ou E em maiúsculas)
"""
nota = 0
while 0 <= nota <= 100:
    nota = int(input())
    if nota == 0:
        print("E")
    elif 1 <= nota <= 35:
        print("D")
    elif 36 <= nota <= 60:
        print("C")
    elif 61 <= nota <= 85:
        print("B")
    elif 86 <= nota <= 100:
        print("A")
    break
