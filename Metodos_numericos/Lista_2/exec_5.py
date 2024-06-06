# Interpolção de Larange

def f(x):
    return x - 2/x

x0 = 1
x1 = 2
x2 = 2.5

# Usando f(1,2)
x = 1.2
l1 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
l2 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
l3 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))

p = f(x0)*l1 + f(x1)*l2 + f(x2)*l3
dif = (p - f(x))
if dif < 0: dif *= -1 

print(f'p(1.2) = {p} f(1.2) = {f(x)} diferença = {dif}')

# Usando f(2,2)
x = 2.2
l1 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
l2 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
l3 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))

p = f(x0)*l1 + f(x1)*l2 + f(x2)*l3
dif = (p - f(x))
if dif < 0: dif *= -1 

print(f'p(2.2) = {p} f(2.2) = {f(x)} diferença = {dif}')