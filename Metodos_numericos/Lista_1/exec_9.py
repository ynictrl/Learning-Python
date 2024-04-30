# f(x) = 1 + 3(x − 1) + 3(x − 1)2 + (x − 1)3
# f(x) = 1 + 3(x + 1) − 3(x + 1)2 + (x + 1)3

def pol(x):
    y1 = 1 + 3*(x-1) + 3*(x-1)**2 + (x-1)**3
    y2 = 1 + 3*(x+1) - 3*(x+1)**2 + (x+1)**3

    return y1, y2

valores = pol(0)

if valores[0] == valores[1]:
    res = 'Iguais'
else:
    res = 'Diferentes'

print(valores, res)