# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uuma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

lista_mult = []


def mult(*args):
    res = 1
    for i in args:
        res = i * res

    # print(res)
    return res

def evenOrOdd(a): # par ou ímpar
    ...
    if (a % 2) == 0: # par
        return 'par'
    else: # ímpar
        return 'ímpar'


# resultado = mult(*lista_mult)
# print(mult(*lista_mult))

while True:
    opcao = input('Digite: \nQualquer número \nMostrar (r)esultados \nLimpar (l)ista\n') # pergunta

    if opcao == 'r': # mostrar resultado
        if lista_mult != []: # veriicar se a lista esta vazia
            print(f'\nNúmeros multiplicados: {mult(*lista_mult)} \nParidade: {evenOrOdd(mult(*lista_mult))}\n')
        else:
            print('\nNão há números!\n')
    elif opcao == 'l':
        lista_mult.clear()
    else:
        try:
            lista_mult.append(float(opcao)) # verificar se é um num
            print(lista_mult)
        except:
            print('\nDigite um número!\n')

