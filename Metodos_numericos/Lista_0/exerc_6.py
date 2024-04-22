# sequencia dada pelo usuário
num = [4, 2, 15, 15, 15, 3, 7, 7, 7, 7, 2]

def numero_triplas(numeros):
    count = 0 # contagem
    pred = 0 # antecessor
    tripla = 0

    for i in numeros:
        if i != pred:
            count = 0

        pred = i
        count += 1

        if count >= 3:
            tripla += 1

    return (f'A seqüência dada contém {tripla} tripla(s).')

print(numero_triplas(num))