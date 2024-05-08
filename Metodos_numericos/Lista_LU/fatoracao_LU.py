import numpy as np

lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# print(type(matriz), type(lista), np.dot(matriz, lista))

#   sistema(Ax = B)
#   [a11, a12, a13]   [x1]   b1
#   [a21, a22, a23] * [x2] = b2
#   [a31, a32, a33]   [x3]   b3

#   multiplicador
#   l2 = l2 - (a21/a11)*l1
#   m21 = a21/a11 |  m31 = a31/a11 |  m32 = a32/a22 |

#   matriz triangular superior(Upper)
#       [u11, u12, u13]
#   U = [  0, u22, u23]
#       [  0,   0, u33]

#   matriz triangular inferior(lower)
#       [  1,   0,   0]
#   L = [m21,   1,   0]
#       [m31, m32,   1]

#   A  = LU
#   Ax = B
#   L(Ux) = B
#   Ux = y
#   Ly = B

# -------------------------------

# eliminação de gauss

# l2 = l2 - (a21/a11)*l1
# print(matriz[1][0]/matriz[0][0],matriz[1][1]/matriz[0][1],matriz[1][2]/matriz[0][2])

# m10 = matriz[1][0]/matriz[0][0]
# matriz[1][0] -= (m10)*matriz[0][0]
# matriz[1][1] -= (m10)*matriz[0][1]
# matriz[1][2] -= (m10)*matriz[0][2]

# m20 = matriz[2][0]/matriz[0][0]
# matriz[2][0] -= (m20)*matriz[0][0]
# matriz[2][1] -= (m20)*matriz[0][1]
# matriz[2][2] -= (m20)*matriz[0][2]

# m21 = matriz[2][1]/matriz[1][1]
# matriz[2][0] -= (m21)*matriz[1][0]
# matriz[2][1] -= (m21)*matriz[1][1]
# matriz[2][2] -= (m21)*matriz[1][2]

def gauss(m):
    m10 = m[1][0]/m[0][0]
    for i in range(3):
        m[1][i] -= (m10)*m[0][i]

    m20 = m[2][0]/m[0][0]
    for i in range(3):
        m[2][i] -= (m20)*m[0][i]

    m21 = m[2][1]/m[1][1]
    for i in range(3):
        m[2][i] -= (m21)*m[1][i]

    return m, m10, m20, m21


# print(gauss(matriz))
# -----------------------------------

#   Exemplo
#   Ax = B
#   [ 2,  3, -1]   [x1]    2
#   [ 4,  4, -1] * [x2] = -1
#   [-2, -3,  4]   [x3]    1

B = [2, -1, 1] 

A = np.array([[ 2,  3, -1],
              [ 4,  4, -1],
              [-2, -3,  4]]) 

U = A.copy() # deep copy: copia que não altera o original
U = gauss(U)[0]

L = np.zeros((3,3))
L[1][0] = gauss(A.copy())[1]
L[2][0] = gauss(A.copy())[2]
L[2][1] = gauss(A.copy())[3]
for i in range(3):
    L[i][i] = 1

print(A, U, L, sep='\n')

#   L(Ux) = B
#   [ 1, 0, 0]   [ 2, 3,-1]   [x1]    2
#   [ 2, 1, 0] * [ 0,-2, 1] * [x2] = -1
#   [-1, 0, 1]   [ 0, 0, 3]   [x3]    1

#   Ux = y
#   Ly = B
#   [ 1, 0, 0]   [y1]    2
#   [ 2, 1, 0] * [y2] = -1
#   [-1, 0, 1]   [y3]    1

#   encontrar y

y = np.ones(3)
y[0] = B[0]/L[0][0]
y[1] = (B[1] - L[1][0]*y[0])/L[1][1]
y[2] = (B[2] - L[2][0]*y[0]- L[2][1]*y[1])/L[2][2]

print('y:', y)

#   Ux = y
#   [ 2, 3,-1]   [x1]    2
#   [ 0,-2, 1] * [x2] = -5
#   [ 0, 0, 3]   [x3]    3

#   encontrar x

x = np.ones(3)
x[2] = y[2]/U[2][2]
x[1] = (y[1] - U[1][2]*x[2])/U[1][1]
x[0] = (y[0] - U[0][2]*x[2]- U[0][1]*x[1])/U[0][0]

print('x:', x)
