# Interpolção de Larange

# configuração para outputs melhores no artigo, pode ser ignorado
# from sympy import init_printing
# init_printing(use_latex='png', scale=1.05, order='grlex',
#               forecolor='Black', backcolor='White', fontsize=10)

from sympy import integrate, Symbol, dsolve, Function, diff, Eq

x = Symbol('x')
expr = 1 / (14 - 4*x)

integral = integrate(expr, (x, 1, 3)).evalf()

def f(a):
    return 1 / (14 - 4*a)

#trapeio, intervalo, altura, area
t = [2, 4, 8, 16]
i = [1, 3]
h = []
a = []
erro = []

h.append((i[1]-i[0])/t[0])
a.append(h[0]*(f(0) + f(1))/2)
erro.append(integral-a[0])

h.append((i[1]-i[0])/t[1])
a.append(h[1]*(((f(0) + f(1))/2) + f(h[1])))
erro.append(integral-a[1])

h.append((i[1]-i[0])/t[2])
a.append(h[2]*(((f(0) + f(1))/2) + f(h[2]) + f(h[2]*2) + f(h[2]*3)))
erro.append(integral-a[2])

h.append((i[1]-i[0])/t[3])
a.append(h[3]*(((f(0) + f(1))/2) + f(h[3]) + f(h[3]*2) + f(h[3]*3) + f(h[3]*4) + f(h[3]*5) + f(h[3]*6) + f(h[3]*7)))
erro.append(integral-a[3])

# h.append((i[1]-i[0])/t[4])
# a.append(h[4]*(((f(0) + f(1))/2) + f(h[4]) + f(h[4]*2) + f(h[4]*3) + f(h[4]*4) + f(h[4]*5) + f(h[4]*6) + f(h[4]*7) + f(h[4]*8) + f(h[4]*9) + f(h[4]*10) + f(h[4]*11) + f(h[4]*12) + f(h[4]*13) + f(h[4]*14) + f(h[4]*15) + f(h[4]*16)))
# erro.append(integral-a[4])

print(h, a, erro, sep='\n')

# o erro aumenta ligeiramente mas se mantem

