"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        'Desculpe, você deixou campus vazios.'
"""

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome and idade:
    nome_invertido = nome[::-1]
    nome_espaços = " " in nome
    num_letras = len(nome)
    primeira_letra = nome[0]
    ultima_letras = nome[len(nome) - 1]

    print(f'Seu nome é {nome}\n'
        f'Seu nome invertido é {nome_invertido}\n'
        f'Seu nome contém espaços? {nome_espaços} \n'
        f'Seu nome tem {num_letras} letras\n'
        f'A primeira letra do seu nome é {primeira_letra}\n'
        f'A ultima letra do seu nome é {ultima_letras}')
else:
    print('Desculpe, você deixou campus vazios.')