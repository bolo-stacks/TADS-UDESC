#  Exercício 1
'''
faça um programa em python Escreva um algoritmo que permita a leitura de 7 nomes e coloque em uma lista. Exiba a lista de trás para frente, exibindo no início o último nome informado e o ao final da lista o primeiro. Exiba um nome a cada linha.
'''

# Inicialize uma lista vazia para armazenar os nomes
nomes = []

# Faça um loop para ler 7 nomes
for i in range(7):
    nome = input()
    nomes.append(nome)

# Inverta a lista de nomes
nomes_invertidos = nomes[::-1]

# Exiba os nomes de trás para frente, um por linha
for nome in nomes_invertidos:
    print(nome)


# Exercício 2
'''
Crie um programa em Python para ler uma frase, separar palavra por palavra e exibir cada palavra em uma linha.
'''

# Solicite ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Separe a frase em palavras usando o espaço como separador
palavras = frase.split()

# Exiba cada palavra em uma linha
for palavra in palavras:
    print(palavra)


# Exercício #3
'''
Faça um algoritmo que leia o nome de 20 pessoas e exiba ao final a lista de nomes em ordem alfabética. Exiba um nome por linha.
'''

# Inicialize uma lista vazia para armazenar os nomes
nomes = []

# Faça um loop para ler os nomes de 20 pessoas
for i in range(20):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    nomes.append(nome)

# Ordene a lista de nomes em ordem alfabética
nomes_ordenados = sorted(nomes)

# Exiba os nomes em ordem alfabética, um por linha
for nome in nomes_ordenados:
    print(nome)

# Exercício 4
'''
Fazer um programa para ler 10 strings contendo números ou expressões aritméticas. Após ler os strings, faça o Python avaliar as expressões e somar o resultado de todas as 10. Exiba o valor da soma ao final como ponto flutuante (float).
'''

expressoes = []
for i in range(10):
    expressao = input()
    expressoes.append(expressao)
soma = 0.0
for expressao in expressoes:
    resultado = eval(expressao)
    soma += resultado
print(f"{float(soma):.2f}")


# Exercicio 5

'''
Qual a saída do seguinte programa?

Trecho de Código: busca substring (Python)

str1 =='Universidade do Estado de Santa Catarina'

valor = str1.find("Catarina")

# Output
print(valor)

Resposta: 32
'''

# Exercicio 6

'''
Faça um programa em Python para inverter a primeira metade de uma string. O programa deve ler uma string, inverter a primeira metade (à esquerda) e salve a string com a nova configuração.
'''

# Solicite ao usuário que digite uma string
string = input("Digite uma string: ")

# Verifique se a string tem pelo menos 2 caracteres
if len(string) < 2:
    print("A string deve ter pelo menos 2 caracteres.")
else:
    # Calcule o ponto médio da string
    meio = len(string) // 2

    # Inverta a primeira metade da string
    primeira_metade_invertida = string[:meio][::-1]

    # Combine a primeira metade invertida com a segunda metade
    nova_string = primeira_metade_invertida + string[meio:]

    # Exiba a nova string com a primeira metade invertida
    print("Nova string com a primeira metade invertida:", nova_string)
