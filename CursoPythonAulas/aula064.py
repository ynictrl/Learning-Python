# gerador de cpf aleatorio

import random

quant_cpf = 100

for _ in range(quant_cpf):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    #primeiro digito
    multiplicador_1 = 10
    digito_1 = 0

    for i in range((len(nove_digitos))):
        digito_1 += int(nove_digitos[i]) * multiplicador_1 #try/ except
        multiplicador_1 -= 1

    digito_1 = digito_1 * 10
    digito_1 = digito_1 % 11    
    if digito_1 > 9:
        digito_1 = 0
    else:
        digito_1 = digito_1
    #print(f'Primeiro digito: {digito_1}')

    #segundo digito
    multiplicador_2 = 11
    digito_2 = 0
    dez_digitos = nove_digitos + str(digito_1)

    for i in range((len(dez_digitos))):
        digito_2 += int(dez_digitos[i]) * multiplicador_2 #try/ except
        multiplicador_2 -= 1

    digito_2 = digito_2 * 10
    digito_2 = digito_2 % 11    
    if digito_2 > 9:
        digito_2 = 0
    else:
        digito_2 = digito_2
    #print(f'Segundo digito: {digito_2}')

    # CPF gerado

    cpf = dez_digitos + str(digito_2)
    print('CPF:', cpf)
