"""
args - Argumentos não nomeados
* - *args (empacotamento e desmpacotamento)
"""
# Lembre-te de dempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args): # *args empacota oq eu enviar para a função dentro de uma tupla
    total = 0
    for numero in args:
        total += numero
    # print(total)
    return total #retorn é diferente de print!

soma(1, 2, 3, 4, 5, 6)

soma_1_2_3 = soma(1, 2, 3)
soma_4_5_6 = soma(4, 5, 6)

numeros = 1, 2, 3, 4, 5
outra_soma = soma(*numeros) # desempacotamento
print(outra_soma)

print(sum(numeros)) # função sum soma os elementos
