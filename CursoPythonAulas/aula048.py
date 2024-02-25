"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou no índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         01234
#        -54321  
string = 'ABCDE' # 5 caracteres (len)
#print(bool([])) # false
#print(lista, type(lista))

#       -5   -4     -3        -2   -1
#        0    1      2         3    4
lista = [123, True, 'Nicolas', 1.2, []]
lista[-3] = 'Maria'
print(lista[2], type(lista[2]))

del lista[-2] # não é com removar quando tem muitos eletemntos
print(lista)

lista.append(50) # adciona no ultimo
lista.append(50)
lista.pop() # remove o ultimo
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)

lista.insert(0, 'AAA')
print(lista, 'Adcionado', lista[0])

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_1 = ['1', 1, 1.0]
#lista_2 = lista_1 # afeta a lista 2 ao mudar lista 1
lista_2 = lista_1.copy() # não afeta a lista 2 ao mudar lista 1

lista_1[0] = 'AAA'
print(lista_1)
print(lista_2)