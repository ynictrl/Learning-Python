import numpy as np

# matriz fornecida pelo usuário
matriz = np.array([[0,   1,  2,  3],
                   [4,   5,  6,  7],
                   [8,   9, 10, 11],
                   [12, 13, 18, 15]])

def maior_valor(n):
    N,M = n.shape
    pred = 0

    for i in range(N):
        for j in range(M):
            if n[i, j] > pred:
                pred = n[i, j]

    return (pred)

print(maior_valor(matriz))