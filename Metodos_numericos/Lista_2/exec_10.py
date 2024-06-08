# minimos quadrados

import numpy as np

#(-4,3),(-1,-1),(0,0),(2,1),(3,2)

x = [-4., -1., 0., 2., 3.]
y = [ 3., -1., 0., 1., 2.]

x2 = 0
for i in x:
    x2 += float(i**2)

x3 = 0
for i in x:
    x3 += float(i**3)

x4 = 0
for i in x:
    x4 += float(i**4)

yx1 = 0
for i in range(len(x)):
    yx1 += float(y[i] * x[i])

yx2 = 0
for i in range(len(x)):
    yx2 += float(y[i] * x[i]**2)

M = np.array([[x4, x3,     x2,     yx2   ],
              [x3, x2,     sum(x), yx1   ],
              [x2, sum(x), len(x), sum(y)]])
print(M)

def gauss(m):
    m00 = m[0][0]
    m[0][0] /= m00
    m[0][1] /= m00
    m[0][2] /= m00
    m[0][3] /= m00
    print(m)

    m10 = m[1][0]
    print(m10)
    m[1][0] = m10 * m[0][0] - m[1][0]
    m[1][1] = m10 * m[0][1] - m[1][1]
    m[1][2] = m10 * m[0][2] - m[1][2]
    m[1][3] = m10 * m[0][3] - m[1][3]
    print(m)

    m20 = m[2][0]
    m[2][0] = m20 * m[0][0] - m[2][0]
    m[2][1] = m20 * m[0][1] - m[2][1]
    m[2][2] = m20 * m[0][2] - m[2][2]
    m[2][3] = m20 * m[0][3] - m[2][3]
    print(m)
    
    m11 = m[1][1]
    m[1][0] /= m11
    m[1][1] /= m11
    m[1][2] /= m11
    m[1][3] /= m11
    print(m)

    m21 = m[2][1]
    m[2][0] = m21 * m[1][0] - m[2][0]
    m[2][1] = m21 * m[1][1] - m[2][1]
    m[2][2] = m21 * m[1][2] - m[2][2]
    m[2][3] = m21 * m[1][3] - m[2][3]
    print(m)

    m01 = m[0][1]
    m[0][0] -= m01 * m[1][0]
    m[0][1] -= m01 * m[1][1] 
    m[0][2] -= m01 * m[1][2] 
    m[0][3] -= m01 * m[1][3]
    print(m)

    m22 = m[2][2]
    m[2][0] /= m22
    m[2][1] /= m22
    m[2][2] /= m22
    m[2][3] /= m22
    print(m)

    m12 = m[1][2]
    m[1][0] -= m12 * m[2][0]
    m[1][1] -= m12 * m[2][1]
    m[1][2] -= m12 * m[2][2]
    m[1][3] -= m12 * m[2][3]
    print(m)

    m02 = m[0][2]
    m[0][0] -= m02 * m[2][0]
    m[0][1] -= m02 * m[2][1]
    m[0][2] -= m02 * m[2][2]
    m[0][3] -= m02 * m[2][3]
    print(m)

    return m

res = gauss(M)[:,3]

print(f'{res[0]}*x**2 + {res[1]}*x + {res[2]}')