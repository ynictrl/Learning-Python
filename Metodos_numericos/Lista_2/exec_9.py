# Interpolção de Larange

from sympy import integrate, Symbol

x = Symbol('x')
expr = x**3

integral = integrate(expr, (x, 1, 3)).evalf()

def f(a):
    return (a**3)

#trapeio, intervalo, altura, area
t = [1, 2, 4, 8]
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

print(h,f'n trapézios: {t}', f'áreas: {a}', f'erros: {erro}', sep='\n')

# o erro alto e diminui 

