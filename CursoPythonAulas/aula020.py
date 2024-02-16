# exercicio: identificar o maior número
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

if n1 > n2:
    print(f'O primeiro número, {n1}, é maior que o segundo, {n2}')
elif n2 > n1:
    print(f'O segundo número, {n2}, é maior que o primeiro, {n1}')
else:
    print(f'Os dois números, {n1} e {n2} são iguais')