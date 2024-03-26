import numpy as np

a = np.array([[0,   1,  2,  3],
              [4,   5,  6,  7],
              [8,   9, 10, 11],
              [12, 13, 14, 15]])

N,M = a.shape

print(N, M)
pred = 0

for i in range(N):
    for j in range(M):
        if a[i, j] > pred:
            pred = a[i, j]

print(pred)