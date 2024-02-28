"""
#Gerador de cpf
#Algoritimo cpf

CÁLCULO DO PRIMEIRO DEIGITO DO CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
    70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiplicar o resultado por 10:
    301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
    3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
"""
cpf = '74682489070'
primeiros_digitos = cpf[:9]
resultado = 0
multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2] # ou = 10
#lista_digitos = primeiros_digitos.split('')


for i in range((len(primeiros_digitos))):
    resultado += int(primeiros_digitos[i]) * multiplicadores[i] #try/ except
print(f'Soma dos digitos: {resultado}')

resultado = resultado * 10
print(f'Multiplicado por 10: {resultado}')

resultado = resultado % 11
print(f'Resto da divisão por 11: {resultado}')
    
if resultado > 9:
    resultado = 0
else:
    resultado = resultado
print(f'Primeiro digito: {resultado}')

