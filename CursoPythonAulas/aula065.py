"""
Introdução ás funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo de seu código.
Elas podem receeer valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções em Python retornam None (nada)
"""

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print('Olá,', nome)

saudacao('Nicolas')
saudacao('Luiza')
saudacao()