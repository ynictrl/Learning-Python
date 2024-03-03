# excluir/substituir caracters

# primeiro jeito
cpf = '180.286.367-21'.replace('.', '').replace('-', '') # oq substituir , pelo oq substituir
print(cpf)

# segundo jeito
import re

entrada = input('CPF [180.286.367-21]')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
    
    )
print(cpf)

###

import sys
entrada = input('entrada: ')
entrada_repetida = entrada == entrada[0] * len(entrada)

if entrada_repetida:
    print('Você enviou dados repetidos')
    sys.exit()