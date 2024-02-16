# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# 0 0.0 '' False
# tipo None: não existe, não valor

entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha:' )

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True) #para no false e checa mais nada
print(True and bool('') and True)