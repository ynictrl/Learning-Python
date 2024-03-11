# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# value - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Nicolas',
    'sobrenome': 'Gomes',
    #'idade': 666
}

# len
print(len(pessoa))

# keys
print(list(pessoa.keys()))

# values
print(list(pessoa.values()))

# items
print(list(pessoa.items()))

# setDefault
pessoa.setdefault('idade', 19)
print(pessoa['idade'], f'\n{pessoa}\n')

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# -------------------------------------

# copy

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy() # copia pelo método
d2 = copy.copy(d1) # copia pela biblioteca(Shallow Copy)(não copia os subníveis)
d2 = copy.deepcopy(d1) # copia pelo biblioteca(Deep Copy)(copia os subníveis)

d2['c1'] = 7
d2['l1'][1] = 9

print(d1)
print(d2, '\n')

# -------------------------------------

pessoa = {
    'nome': 'Nicolas',
    'sobrenome': 'Gomes',
    #'idade': 666
}

# get
print(pessoa['nome'])
print(pessoa.get('idade', 'Não existe'))

# pop

nome = pessoa.pop('nome')
print(nome)
print(pessoa)

# popitem

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

# update
 
pessoa.update({
    'nome': 'novo valor',
    'idade': '777',
})
# pessoa.update(nome='novo valor', idade=30)

# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]

# pessoa.update(lista)
# pessoa.update(tupla)

print(pessoa)