num = 16
res = 0
i = 1
impares = [] 

while res < num: 
    impares.append(i)
    res = sum(impares)
    
    print(res, impares)

    i += 2

if res == num:
    print(f'{num} é um quadrado perfeito!')
else:
    print(f'{num} não é um quadrado perfeito!')
