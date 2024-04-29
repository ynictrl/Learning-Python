# Newton-Raphson
import numpy as np

i_i = 0.8
i_f = 1.6

break_list = np.linspace(i_i, i_f, 100)

def f(x):
    return np.cos(x) + 1 - x

def der_f(x):
    return -np.sin(x) - 1

def g(x):
    return x - (f(x)/der_f(x))

iteracoes = 0
y_list = []

for i in break_list:
    # print(i)
    if i == break_list[0]:
        y = g(i)
    else:
        y = g(y)

    iteracoes += 1
    if y in y_list:# parar quando repetir
        print(f'Raiz de (cos(x) + 1 - x) = {y} | interações: {iteracoes}')
        break

    y_list.append(y)
