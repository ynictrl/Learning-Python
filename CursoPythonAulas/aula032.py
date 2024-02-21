"""
Faça um programa que peça ao usurario para digitar um numero inteiro, 
informe se este número é par ou ímpar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""

num_str = input('Digite um número inteiro:')

try: # ou num_str.isdigit():
    num_int = int(num_str)
    if (num_int % 2) == 0:
        print(f'O número {num_int} é par')
    else:
        print(f'O número {num_int} é ímpar')
except:
    print('Não é um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no hórario
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas_str = input('Que horas são?')

try:
    horas_int = int(horas_str)
    if   0 < horas_int and horas_int < 12:
        print(f'Bom dia')
    elif 11 < horas_int and horas_int < 18:
        print(f'Boa tarde')
    elif 17 < horas_int and horas_int < 24:
        print(f'Boa noite')
    else:
        print('Entrada inválida!')
except:
    print('Entrada inválida!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome:')

if   1 <= len(nome) and len(nome) <= 4:
    print(f'Seu nome, {nome}, é pequeno')
elif 5 <= len(nome) and len(nome) <= 6:
    print(f'Seu nome, {nome}, é normal')
elif len(nome) > 6:
    print(f'Seu nome, {nome}, é muito grande')
else:
    print(f'Digite mais de uma letra')
