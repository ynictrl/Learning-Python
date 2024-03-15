"""
Exercícos uma função encontra o primeiro duplicado considerando o segundo
número como a suplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> não tem duplicados (retorne -1)
        [1, 4, 9, 8, ->9<-, 4, 8] -> (retorne 9)
"""
 
listas_conjuntos = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# ta errado
def find_duplicate_0000(l):
    index_i = 0
    index_k = 0
    duplicados = []

    for i in l: # acessando o index da lista
            
        for k in l: # acessando o index da lista (verificando se a duplicados)

            if index_k != index_i:
                if (k == i):
                    duplicados.append(k)

            index_k += 1

        index_i += 1
        index_k = 0

    if duplicados == []:
        return -1
           
    return duplicados[0]

def find_duplicate(l):
    checked = []
    duplicate_1 = -1

    for i in l:
        if not i in checked:
            checked.append(i)
        else:
            duplicate_1 = i
            break

    return duplicate_1

for lista in listas_conjuntos:
    d = find_duplicate(lista)
    print(f'{lista} -- {d}')