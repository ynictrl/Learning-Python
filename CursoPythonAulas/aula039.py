"""
Iterando strings com while
"""

nome = 'Nicolas'
i = 0
nova_str = ''

while i < len(nome):
    nova_str += f'*{nome[i]}'
    i += 1
nova_str += '*'

print(nova_str)