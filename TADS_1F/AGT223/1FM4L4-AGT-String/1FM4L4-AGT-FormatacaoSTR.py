# Formatação de STRs
print('Meu {} disse "{}!"'.format('amigo', 'olá'))
print('{0} e {1}'.format('cédulas', 'moedas'))
print('{1} e {0}'.format('cédulas', 'moedas'))

# Formatação de variáveis internas
print('Este {objeto} é {adjetivo}.'.format(
    objeto='óculos', adjetivo='muito feio'))

print('Este {1} com {0} é {adjetivo}.'.format(
    'capa', 'celular', adjetivo='lindo'))

# Format com dicionário
tabela = {'idnome': 444, 'cidade': 333, 'rua': 222}
print('nome: {0[idnome]:d} cidade: {0[cidade]:d} rua: {0[rua]:d}'.format(tabela))

# Format tabela com notação
print('N: {idnome:d} C: {cidade:d} R:{rua:d}'.format(**tabela))

# Formatação com f ou F de variáveis ou valores literais.
ano = 2023
disciplina = "Algoritmos"
print(f'No ano de {ano} aprendi {disciplina}')

# 2º Exemplo de Formatação com f ou F de variáveis ou valores literais.
chance = 0.4967
# ano tem nove casas decimais de separação, 5 espaços mais 2023, 0.4967 formatado para 49.67%
print('ano {:-9} tem {:2.2%} de chance.'.format(ano, chance))

# Outras formatações:
# <num> inteiro com sinal
# <int.dec> float real
# u (inteiro sem sinal
# o (octal)
# b (binário
# x hexadecimal
# e notação exponencial
# % porcentagem

# Strings literais formatadas
ano = 2023
disciplina = 'Algoritmos'
print(f'No ano de {ano:o} aprendi {disciplina}')  # ano octal
print(f'No ano de {ano:x} aprendi {disciplina}')  # ano hexadecimal
print(f'No ano de {ano:b} aprendi {disciplina}')  # ano binário

# 2°exemplo de Strings literais formatadas com f, .format e %
ano = 2023
disciplina = 'Algoritmos'
print(f'No ano de {ano:d} aprendi {disciplina}')  # formata integral (int)
# 6 espaços ante de ano e disciplina string
print('No ano de {:-6} aprendi {:s}'.format(ano, disciplina))
print(f'No ano de %5d aprendi %s' % (ano, disciplina))

# Transformar Int ou Float em String:
# str() gera representações de valores legíveis.
# repr() gera representações que o Python lê.
# Exemplo:
print(str(1/7))  # Transforma em string
print(repr(1/7))  # Cria uma representação igual ao valor numérico

# 2° Exemplo:
x = 10 * 3.25
y = 200 * 200
# repr transforma em string o  resultado
s = "x é " + repr(x) + ', e y é ' + repr(y) + '...'
print(s)

# 3° exemplo:
texto = repr('olá\n')
print(texto)

# 4° exemplo
print(repr((x, y, ('xis', 'y'))))

# Concatenação (juntar strings)
print('a' + 'b' + 'c')
strings = ['do', 're', 'mi']
print(strings[0] + strings[1] + strings[2])
s = ''

for i in strings:
    s += i
print(s)

# Concatenação com join
print('a' + 'b' + 'c')
strings = ['do', 're', 'mi']
print(''.join(strings))  # dentro das aspas vai o separador

print('a' + 'b' + 'c')
strings = ['do', 're', 'mi']
print(', '.join(strings))  # dentro das aspas vai o separador

# String parcial
s = 'um dois três quatro cinco'
print(s[8:12])

print(s[::2])  # os pares

print(s[13])  # caractere 13

print(s[::-1])  # de trás pra frente

print(s[11:7:-1])  # seleciona uma palavra e print invertida
