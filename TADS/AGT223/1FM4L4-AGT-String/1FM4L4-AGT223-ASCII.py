# vim aqui dizer que a tabela ascii é 7 bits


# Pegar o código ascii de um caractere ord()
x = 'a'
print(ord(x))

# Mostrar o ascii dos caracteres de uma palavra
str1 = 'Teste'
for i in str1:
    print(ord(i))

# criar uma lista ascii de uma palavra
str1 = 'Teste'
lista = [ord(c) for c in str1]
print(lista)

# Exibir o código ascii transformando ele em bytes com b
print(list(b"Teste"))

#  Exibir o ascii usando o comando de codificação encode
print(list("Teste".encode('ascii')))
