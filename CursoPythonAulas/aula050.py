"""
Exercício 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(lista.index(nome), nome)

for i in range(len(lista)):
    print(i, lista[i])