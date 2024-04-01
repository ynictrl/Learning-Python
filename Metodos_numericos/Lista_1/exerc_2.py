# [ 1, 2, 3, 5, 7, 11, 13, 17...]

num = 10 # valor fornecido pelo usuário

def sequencia_primos(n):
    numeros = []

    i=1
    j=1
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

    return numeros

print(sequencia_primos(num))