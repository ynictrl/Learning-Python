"""
#Gerador de cpf
#Algoritimo cpf

CÁLCULO DO SEGUNDO DEIGITO DO CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF (MAIS O PRIMEIRO DIGITO)
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
    11  10  9  8  7  6  5  4  3  2
    7   4   6  8  2  4  8  9  0  7
    77  40  54 64 14 24 40 36 0  14

Somar todos os resultados:
    77 + 40 + 54 + 64 + 14 + 20 + 40 + 36 + 0 + 14 = 363
Multiplicar o resultado por 11:
    363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
    3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo digito do CPF é 0
"""
cpf = '18028636721'
#nove_digitos = cpf[:9]
#primeiro_digito = cpf[10]
digitos_analisados = cpf[:10]

resultado = 0
multiplicador = 11

for i in range((len(digitos_analisados))):
    resultado += int(digitos_analisados[i]) * multiplicador #try/ except
    multiplicador -= 1
    
print(f'Soma dos digitos: {resultado}')

resultado = resultado * 10
print(f'Multiplicado por 10: {resultado}')

resultado = resultado % 11
print(f'Resto da divisão por 11: {resultado}')
    
if resultado > 9:
    resultado = 0
else:
    resultado = resultado
print(f'Segundo digito: {resultado}')
