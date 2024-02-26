"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (03, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_eneumerada = list(enumerate(lista, start=3))
print(lista_eneumerada)


for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')