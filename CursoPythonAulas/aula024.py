# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  N i c o l a s
# -7-6-5-4-3-2-1

nome = 'Nicolas'
print(nome[2])
print(nome[-5])

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não está em {nome}')