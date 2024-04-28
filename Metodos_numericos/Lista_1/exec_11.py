# f(x) = cos(x) + 1 − x,
# intervalo [0.8, 1.6]
# ε = 10**-12
# 100 iteraçoes

import numpy as np

#função 
def f(x):
    return np.cos(x) + - x

#intervalo
ak = 0.8
bk = 1.6

#lista de f(ck)
yck_list = []

# MÉTODO BISSECÇÃO

for i in range(100):
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

#intervalo
ak = 0.8
bk = 1.6

#lista de f(ck)
yck_list = []

# MÉTODO DA FALSA POSIÇÃO

for i in range(100):
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

