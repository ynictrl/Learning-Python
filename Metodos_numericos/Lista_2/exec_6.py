# Interpolção de Larange

def f(x):
    return x - 2/x

def larange(x, x0, x1, x2):

    l1 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    l2 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    l3 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))

    p = f(x0)*l1 + f(x1)*l2 + f(x2)*l3
    dif = (p - f(x))
    if dif < 0: dif *= -1 

    return print(f'p({x}) = {p} f({x}) = {f(x)} diferença = {dif}')

# Usando f(2,2)
larange(1.2, 1, 2, 2.5)
larange(2.2, 1, 2, 2.5)