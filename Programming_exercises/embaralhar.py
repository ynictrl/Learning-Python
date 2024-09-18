import random
# random - número entre 0 e 1
# numero_0a100 = random.randrange(0, 11)
# print(numero_0a100)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(random.sample(numeros, k=14))
# random.shuffle(numeros)

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = []

for i in range(len(l1)):
    
    if i == 0:
        k = random.randrange(0, len(l1))
        lost = str(k)
    else:
        
        while str(k) in lost:
            k = random.randrange(0, len(l1))
        lost += str(k)
       
    l2.append(l1[k])

print(f'Lista original:    {l1} \nLista embaralhada: {l2}')
