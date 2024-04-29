# Newton-Raphson

N = 91

# RAIZ QUADRADA

y_list = []

def raiz_2(x):
    return x**2 - N

def der_raiz_2(x):
    return 2*x

def g_2(x):
    return x - (raiz_2(x)/der_raiz_2(x))

iteracoes =0
for i in range(10, 100):
    # print(i)
    if i == 10:
        y = g_2(i)
    else:
        y = g_2(y)

    iteracoes += 1
    if y in y_list:# parar quando repetir
        print(f'Raiz quadrada de {N} = {y} | interações: {iteracoes}')
        break

    y_list.append(y)