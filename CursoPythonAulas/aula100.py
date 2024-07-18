import importlib

import aula100_m

print(aula100_m.variavel)

for i in range(10):
    importlib.reload(aula100_m)
    print(i)

print('Fim')