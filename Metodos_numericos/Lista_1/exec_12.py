# Newton-Raphson

N = 5

# RAIZ CUBICA

y_list = []

def raiz_3(x):
    return x**3 - N

def der_raiz_3(x):
    return 3*(x**2)

def g_3(x):
    return x - (raiz_3(x)/der_raiz_3(x))

for i in range(100):

    if i == 0:
        y = g_3(i+1)
    else:
        y = g_3(y)

    if y in y_list:# parar quando repetir
        print(f'Raiz cubica de {N} = {y}')
        break

    y_list.append(y)

#--------------------------------------------
    
# RAIZ A QUARTA

y_list = []

def raiz_4(x):
    return x**4 - N

def der_raiz_4(x):
    return 4*(x**3)

def g_4(x):
    return x - (raiz_4(x)/der_raiz_4(x))

for i in range(100):

    if i == 0:
        y = g_4(i+1)
    else:
        y = g_4(y)

    if y in y_list:# parar quando repetir
        print(f'Raiz a quarta de {N} = {y}')
        break

    y_list.append(y)