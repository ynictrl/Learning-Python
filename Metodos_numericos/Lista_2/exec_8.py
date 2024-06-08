# Interpolção de Larange

from sympy import integrate, Symbol

x = Symbol('x')
expr = 1 / (7 - 2*x)

integral = integrate(expr, (x, 1, 3)).evalf()

def f(a):
    return 1 / (7 - 2*a)

#trapeio, intervalo, altura, area
t = [2, 4, 8, 16, 32, 64]
i = [1, 3]
h = []
a = []
erro = []

h.append((i[1]-i[0])/t[0])
a.append(h[0]*(f(i[0]) + f(i[1]))/2)
erro.append(integral-a[0])

h.append((i[1]-i[0])/t[1])
a.append(h[1]*(((f(i[0]) + f(i[1]))/2) + f(h[1])))
erro.append(integral-a[1])

h.append((i[1]-i[0])/t[2])
a.append(h[2]*(((f(i[0]) + f(i[1]))/2) + f(h[2]) + f(h[2]*2) + f(h[2]*3)))
erro.append(integral-a[2])

h.append((i[1]-i[0])/t[3])
a.append(h[3]*(((f(i[0]) + f(i[1]))/2) + f(h[3]) + f(h[3]*2) + f(h[3]*3) + f(h[3]*4) + f(h[3]*5) + f(h[3]*6) + f(h[3]*7)))
erro.append(integral-a[3])

h.append((i[1]-i[0])/t[4])
f_soma = 0
for j in range(1,16):
    f_soma += f(h[4]*j)
a.append(h[4]*(((f(i[0]) + f(i[1]))/2) + f_soma))
erro.append(integral-a[4])

h.append((i[1]-i[0])/t[5])
f_soma = 0
for k in range(1,32):
    f_soma += f(h[5]*k)
a.append(h[5]*(((f(i[0]) + f(i[1]))/2) + f_soma))
erro.append(integral-a[5])

print(f'n trapézios: {t}', f'áreas: {a}', f'erros: {erro}', sep='\n')

# o erro baixo e aumenta ligeiramente

