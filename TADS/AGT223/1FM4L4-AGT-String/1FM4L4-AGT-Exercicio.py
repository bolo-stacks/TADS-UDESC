
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

# Encontra palavras dentro da STR
if "olá" in str1:
    print("tem 'olá'")


# Verificar e adicionar
if "$" not in str1:
    str1 = str1 + '$'
print(str1)    

# Encontra index na STR
# Se não encontra retorna -1
pos1 = str1.find('m')
pos2 = str1.find("mundo")
print(pos1)
print(pos2)

# Tornar uma STR em list
str4 = "Seja muito bem vindo ao curso TADS"
lista = str4.split() # () definir separador
print(lista)
lista2 = str4.split(' ', 2) # Separa até o Index 2
print(lista2)

# Relembrar list
# len min max sum (comprimento, menor item, maior item, soma)
# lista.append
# lista.count (conta as ocorrências de um item)
# lista.insert (pos, item)
# lista.pop remove o último elemento da list
# lista.remove (remove a primeira ocorrência de um item)
# lista.reverse
# lista.sort ordena crescente

# Copia de lista (mesma posição de memória)
animais = ['vaca', 'cavalo', 'cachorro']
b = animais
b.append('porco')
print(animais)
print(b)

# Cópia parcial (endereço de memória diferente)
c = animais[:2] # Copiando somente os 2 primeiros
print(c)

# Copia parcial 2
num = [0,1,2,3,4,5,6,7,8,9]
copia = num[5:] # Últimos 5
print(copia)
copia2 = num[::2] # Pares
print(copia2)
copia3 = num[1::2] # Impares
print(copia3)
copia4 = num[:] # Todos
print(copia4)

# Copia de lista (lista inteira, posição de memória diferente)
animais = ['vaca', 'cavalo', 'cachorro']
b = animais[:] # Copia do início ao fim mas com endereço de memória diferente
b.append('porco')
print(animais)
print(b)


