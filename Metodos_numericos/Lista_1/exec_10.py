# f(x) = x ∗ cos[(x)/(x − 2)]
# intervalo [1, 1.5]
# ε = 10**-12
# 500 iteraçoes

import numpy as np

#função 
def f(x):
    return x * np.cos((x)/(x - 2))

#intervalo
ak = 1
bk = 1.5

#lista de f(ck)
yck_list = []

# MÉTODO BISSECÇÃO

for i in range(500):
    ck = (bk + ak)/2
    yck = f(ck)

    if yck < 0:
        ak = ck
    elif yck > 0:
        bk = ck

    if yck in yck_list: # parar quando repetir o valor
        print(f'Método: Bissecção | Raíz: {yck} | Iteração: {i}')
        break

    yck_list.append(yck) # adcionar a lista

#-----------------------------------------------------

#função 
def f(x):
    return x*np.sin(x) -1#x * np.cos((x)/(x - 2))

#intervalo
ak = 1
bk = 1.5

#lista de f(ck)
yck_list = []

# MÉTODO DA FALSA POSIÇÃO

for i in range(500):
    ck = bk - (f(bk)*(bk-ak))/(f(bk)-f(ak))
    yck = f(ck)

    if yck < 0:
        ak = ck
    elif yck > 0:
        bk = ck

    if yck in yck_list: # parar quando repetir o valor
        print(f'Método: Falsa posição | Raíz: {yck} | Iteração: {i}')
        break

    yck_list.append(yck) # adcionar a lista

