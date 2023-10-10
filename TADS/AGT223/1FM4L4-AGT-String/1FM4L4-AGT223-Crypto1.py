# https://www.beecrowd.com.br/repository/UOJ_1024.html

'''
Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.
Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.
Saída

Para cada entrada, deve-se apresentar a mensagem criptografada.
'''
# primeiro método
#  Entrada

'''
frase = input()

# Primeira passada
passo1 = ''
for i in frase:
    if i.isalpha():  # verifica se é alfanumérico
        passo1 = passo1 + chr(ord(i)+3)  # Soma 3 posições ao caractere
    else:
        passo1 = passo1 + i
print('passo1:', passo1)


# Segunda passada
passo2 = passo1[::-1]  # inverte o texto
print("passo2:", passo2)

# Terceira passada
meio = int(len(passo2)/2)
passo3 = passo2[:meio]
for i in range(meio, len(passo2)):
    passo3 = passo3 + chr(ord(passo2[i])-1)
print('passo3', passo3)
'''


# segundo método:
# com dicionário
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{|}~"

print(alphabet)

# Entrada
frase = input()

# primeira passada
passo1 = ""
for i in frase:
    if i.isalpha():
        passo1 += alphabet[alphabet.find(i) + 3]
    else:
        passo1 += i
print(f"passo1: '{passo1}'")

# Segunda passada
passo2 = passo1[::-1]
print(f"passo2: '{passo2}'")

# Terceira passada
meio = int(len(passo2)/2)
passo3 = passo2[:meio]

for i in range(meio, len(passo2)):
    passo3 += alphabet[alphabet.find(passo2[i])-1]
print(f"passo3: '{passo3}'")


'''
DEScriptografia (do exercício anterior)
Trecho de Código: Descriptografia 1 (Python)

# Leitura de passo3 (ou continuação do outro código)
passo3 = input()

# terceira passada invertida:
meio = int(len(passo3)/2)
passo2 = passo3[:meio]
for i in range(meio, len(passo3)):
  passo2 += chr(ord(passo3[j]) + 1)
print(f"Novo Passo2: '{passo2}'")

# segunda passada invertida:
passo1 = passo2[::-1]
print(f"Novo Passo1: '{passo1}'")

# primeira passada invertida:
frase = ""
for i in passo1:
  letra  = chr(ord(j) - 3)
  if letra.isalpha():
    frase += letra
  else:
    frase += i
print(f"Frase descriptografada: '{frase}'")



Trecho de Código: Descriptografia 2 (Python)

# Leitura de passo3 (ou continuação do outro código)
passo3 = input()

# terceira passada invertida:
meio = int(len(passo3)/2)
passo2 = passo3[:meio]
for i in range(meio, len(passo3)):
  passo2 += alphabet[alphabet.find(passo3[i]) + 1]
print(f"Novo Passo2: '{passo2}'")

# segunda passada invertida:
passo1 = passo2[::-1]
print(f"Novo Passo1: '{passo1}'")

# primeira passada invertida:
frase = ""
for i in passo1:
  letra  = alphabet[alphabet.find(i) - 3]
  if letra.isalpha():
    frase += letra
  else:
    frase += i
print(f"Frase descriptografada: '{frase}'")

'''
