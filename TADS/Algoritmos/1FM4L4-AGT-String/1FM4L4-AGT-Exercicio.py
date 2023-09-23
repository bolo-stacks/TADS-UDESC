
str1 = 'olá' + 'Mundo'
str2 = str1 * 3
str3 = str1[2]
tamanho = len(str2)

print(str3)
print(tamanho)
print(str2[4]) # Retorna index da string (á)

# Trocando um index da STR
# ele cria outra string na memória
print(str1)
print(str1[3])
str1=str1.replace('M','m')
print(str1)