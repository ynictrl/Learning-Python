"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o paramêtro, o valor padrão será usado
Refatorar: editar o seu código
"""

def soma(x, y, z=None): # none é não valor // tds os parametros após um par. com valor padrão precisam ter um val. pad.
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} {z=}', x + y + z)

soma(1, 2)
soma(3, 6)
soma(100, 200)
soma(11, 22, 33)