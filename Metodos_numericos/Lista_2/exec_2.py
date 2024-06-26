# Métodos Jacobi e Gauss-Seidel

import numpy as np

M = np.array([[10.0,  5.0,  2.0,  1.0,  18.0],
              [ 5.0, 10.0, -3.0,  2.0,  14.0],
              [ 2.0, -3.0, 12.0, -5.0,  -9.0],
              [ 1.0,  2.0, -5.0, 12.0,  10.0]])

A = M[:,:4]
B = M[:,4]

# Método Jacobi

# x(0) = (2,2,2,2)
#x1 = (b1-[a12x2(0)+a13x3(0)+a14x4(0)+...+a1nxn(0)])/a11
#x2 = (b2-[a21x1(0)+a23x3(0)+a24x4(0)+...+a2nxn(0)])/a22
#x3 = (b3-[a31x1(0)+a32x2(0)+a34x4(0)+...+a3nxn(0)])/a33

x0 = [2,2,2,2]
x1 = []

# while
# i = 0
# while True:
#     x1 = []
#     x1.append((B[0] - (A[0][1]*x0[1] + A[0][2]*x0[2] + A[0][3]*x0[3]))/A[0][0])
#     x1.append((B[1] - (A[1][0]*x0[0] + A[1][2]*x0[2] + A[1][3]*x0[3]))/A[1][1])
#     x1.append((B[2] - (A[2][1]*x0[1] + A[2][0]*x0[0] + A[2][3]*x0[3]))/A[2][2])
#     x1.append((B[3] - (A[3][1]*x0[1] + A[3][2]*x0[2] + A[3][0]*x0[0]))/A[3][3])

#     if(x0 == x1):
#         break

#     i += 1
#     x0 = x1
    
# print(f'iterações: {i}')
# print(f'x: {x1}')

# for
for i in range(6):
    x1 = []
    x1.append((B[0] - (A[0][1]*x0[1] + A[0][2]*x0[2] + A[0][3]*x0[3]))/A[0][0])
    x1.append((B[1] - (A[1][0]*x0[0] + A[1][2]*x0[2] + A[1][3]*x0[3]))/A[1][1])
    x1.append((B[2] - (A[2][1]*x0[1] + A[2][0]*x0[0] + A[2][3]*x0[3]))/A[2][2])
    x1.append((B[3] - (A[3][1]*x0[1] + A[3][2]*x0[2] + A[3][0]*x0[0]))/A[3][3])

    if(x0 == x1):
        print(i)
        break

    x0 = x1
    print(x1, sep='\n')

y = []
# prova real
for j in range(4):
    
    y.append(A[j][0]*x1[0] +  A[j][1]*x1[1] +  A[j][2]*x1[2] +  A[j][3]*x1[3])

print(f'resultado com 6 iterações: {y}')
