# Formatação de STRs
print('Meu {} disse "{}!"'.format('amigo', 'olá'))
print('{0} e {1}'.format('cédulas', 'moedas'))
print('{1} e {0}'.format('cédulas','moedas'))

# Formatação de variáveis internas
print('Este {objeto} é {adjetivo}.'.format(objeto='óculos', adjetivo='muito feio'))

print('Este {1} com {0} é {adjetivo}.'.format('capa','celular',adjetivo='lindo'))

# Format com dicionário
tabela = {'idnome':444, 'cidade':333, 'rua':222}
print('nome: {0[idnome]:d} cidade: {0[cidade]:d} rua: {0[rua]:d}'.format(tabela))

# Format tabela com notação
print('N: {idnome:d} C: {cidade:d} R:{rua:d}'.format(**tabela))
