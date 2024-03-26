numbers = [4, 2, 15, 15, 15, 3, 7, 7, 7, 7, 2]

count = 0 # contagem
pred = 0 # antecessor
tripla = 0

for i in numbers:
    if i != pred:
        count = 0

    pred = i
    count += 1

    if count >= 3:
        tripla += 1

print(f'A seqüência dada contém {tripla} tripla(s).')