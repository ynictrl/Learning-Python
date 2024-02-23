"""Calculadora com while"""

while True:

    n1 = input('Digite um número:')
    op = input('Digite um operador: [+] [-] [*] [/]')
    n2 = input('Digite outro número:')
    res = 0
    numeros_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
        operador_valido = None

    if numeros_validos is None:
        print('Números inválidos')
        continue

    if (op not in "+-*/") and (len(op) > 1):
        print('Operador inválido!')
        continue

    print('Resultado:')
    if   op == '+':              
        res = n1_float + n2_float
    elif op == '-':
        res = n1_float - n2_float
    elif op == '*':
        res = n1_float * n2_float
    elif op == '/':
        res = n1_float / n2_float
    else:
        print('Não pode chegar aqui')

    print(f'{n1} {op} {n2} = {res}')

    ###
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break