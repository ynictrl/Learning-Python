# manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Nicolas'
pessoa['sobrenome'] = 'Gomes'

print(pessoa[chave])

pessoa[chave] = 'Luiza'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('não existe')
else:
    print(pessoa['sobrenome'])