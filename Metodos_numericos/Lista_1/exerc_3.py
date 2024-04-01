num = 16 # valor fornecido pelo usuário

def quadrado_perfeito(n):
    res = 0
    i = 1
    impares = [] 

    while res < n: 
        impares.append(i)
        res = sum(impares)
        
        # print(res, impares)

        i += 2

    if res == n:
        return f'{n} é um quadrado perfeito!'
    else:
        return f'{n} não é um quadrado perfeito!'

print(quadrado_perfeito(num))
