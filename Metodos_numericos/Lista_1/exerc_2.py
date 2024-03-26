# [ 1, 2, 3, 5, 7, 11, 13, 17...]
numeros = []

i=1
j=1
n = 10
while len(numeros) != n:
    count = 0
    for j in range(2, i):
            
        res = i%j
        if (res == 0 and i != j):
            count += 1
        j += 1

    if count == 0:
        numeros.append(i)
        
    i += 1

print(numeros)