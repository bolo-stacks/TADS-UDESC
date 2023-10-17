'''
A agenda deve ser capaz de:

Incluir registro (Lista com mais de um telefone para cada nome)
Excluir registro
Buscar número a partir do nome
Listar todos
'''


'''
Instruções básicas de Tuplas e dicionários para completar a proposta do programa comercial da agenda.
'''

'''
Lista: list 
contato = ['Tiago', '9999-9999']

Tupla: tuple
contato = ('Tiago', '9999-9999')

Dicionário: dict
contato = {'Tiago' : '9999-9999'}

Conjunto: set
contato = {1, 2, 3, 4, 5}
'''

#
#
# 1) Listas

# Como guardar os nomes e telefones com lista?

contatos_lista = ['Thiago', 'Jordan', 'Maurício']
telefones_lista = ['9999-9999', '9999-9998', '8888-7777']

type(contatos_lista)

# Para conectar nomes à telefones utiliza-se index (posição)

#
#
# 2) Tuplas (listas imutáveis com () em vez de [])

# Tupla Exemplo: p1 = (2,3)

contatos_tupla = [('Thiago', '9999-9999'), ('Inácio', '8888-8888')]

type(contatos_tupla)

# Como acessar os valores da tupla?

ver_contato = (contatos_tupla[0][0])

#
#
# 3) Dicionário {}

contatos_dicionario = {'Jordan': '9999-9999'}

type(contatos_dicionario)

# Transformar listas em dicionário

contatos_dicionario_lista = dict(contatos_dicionario)

# Imprimir um item do dicionário (esse formato mostra error se não encontrado)

print(contatos_dicionario['Jordan'])

# Impressão com msg de 'error' escolhido previamente.

print(contatos_dicionario.get('Jordan', 'Contato não encontrado'))

# Retornar se um nome está no dicionário com bool.

print('Jordan' in contatos_dicionario)

# Para retornar os dados que estão após os dois pontos : no dicionários devemos utilizar values() que irá retornar bool.

print('9999-9999' in contatos_dicionario.values())

# Adicionar valores ao dicionário não é utilizado append(), é só atribuir um valor a variável.

contatos_dicionario['André'] = '9999-9998'
print(contatos_dicionario)

# Alterar um contato
contatos_dicionario['Jordan'] = '9898-9898'

# Excluir contato do dicionário com msg de erro padrão do python

# del contatos_dicionario['Jordan']
print(contatos_dicionario)

# Remoção com método pop com msg de erro customizada
# pop(<chave>, <string de erro>):

# print(contatos_dicionario.pop('Jordan', 'Contato não encontrado'))

# print(contatos_dicionario.pop('André', 'Contato não encontrado'))

print("dicionário vazio", contatos_dicionario)

# Compreensão de dicionário:
# Adicionar número a mais nos telefones.

# Solução 1), com for:

for i in contatos_dicionario:
    contatos_dicionario[i] = '9' + contatos_dicionario[i]
print(contatos_dicionario)

# Solução 2) usando compreensão de dicionários.

contatos_dicionario = {
    nome: '5'+contatos_dicionario[nome] for nome in contatos_dicionario}

print(contatos_dicionario)


'''
Conjuntos
'''

#
#
# 4) Conjuntos, set = {}

# Não contém elementos repetidos, não é possível modificar, utilizados também em operações matemáticas.

# Ex set:

conjunto = {1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 1, 2, 3, 8, 9, 9, 0}

print("\n", conjunto, "\n")

# Transformar lista em set:

minha_lista = [1, 2, 3, 4, 5]
conjunto_lista = set(minha_lista)
print(conjunto_lista, "\n")

# Retornar o tamanho do conjunto com len:

tamanho = len(conjunto)
print(tamanho, '\n')

# Retornar tamanho do set com for:

for i in conjunto:
    print(i)
print('\n')

# Comparar sets:

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {1, 2, 3, 4, 5}
print(conjunto_1 == conjunto_1, '\n')

# Imprimir se conjunto está contido (possui os mesmos elementos no set)

conjunto_3 = {1, 2, 3, 4, 5, 6}
conjunto_4 = {5, 4, 3, 2, 1}
print(conjunto_3 < conjunto_4, "\n")
print(conjunto_3 > conjunto_4, '\n')

# União de sets método com |:

conjunto_5 = {6, 7, 8, 9, 0}
print(conjunto_4 | conjunto_5, '\n')

# União de sets método com union:

conjunto_uniao = conjunto_4.union(conjunto_5)

print(conjunto_uniao, '\n')

# Método 1 de Intersecção de set &, verifica elementos que se existem em ambos:

print(conjunto_3 & conjunto_5, '\n')

# Método 2 de Intersecção de set com .intersection:

conjunto_9 = conjunto_3.intersection(conjunto_5)
print(conjunto_9, '\n')

# Diferença em sets com - :

print(conjunto_3 - conjunto_5, '\n')

# Diferença com difference:

conjunto_8 = conjunto_3.difference(conjunto_5)

print(conjunto_8, '\n')

# Outras operações com set:

# União: |= e update()

# Cópia de set: c2 = c1, c2 = c1.copy()

# Adicionar: add(), c1.add(10)

# Remover: c1.remove(10)

# descartar: c1.discard(10)
