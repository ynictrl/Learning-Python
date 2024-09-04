# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def exibir(lista):
    for item in lista:
        print(item)
    print()

# poderia criar um package com modulo e __init__...

import copy

novos_produtos = copy.deepcopy(produtos)

for i in range(len(novos_produtos)):
    novos_produtos[i]['preco'] *= round(1.1)
exibir(novos_produtos)

#------------------------------------

produtos_ordenados_por_nome = copy.deepcopy(produtos)

l1 = sorted(produtos_ordenados_por_nome, reverse=True, key=lambda item: item['nome'])

exibir(l1)

#------------------------------------

produtos_ordenados_por_preco = copy.deepcopy(produtos)

l2 = sorted(produtos_ordenados_por_preco, key=lambda i: i['preco'])

exibir(l2)