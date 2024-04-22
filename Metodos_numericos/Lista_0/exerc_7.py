num = 5 # número fornecido pelo usuário

def ast_for(n):
    asteriscos_for = ''
    for i in range(n):
        asteriscos_for += '*'

    return asteriscos_for

def ast_while(n):
    asteriscos_while = ''
    j = 0
    while j < n:
        asteriscos_while += '*'
        j += 1
    
    return asteriscos_while

print(f'for:{ast_for(num)} | while:{ast_while(num)}')