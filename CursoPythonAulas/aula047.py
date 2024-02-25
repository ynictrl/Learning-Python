"""
Faça um jogo para que o usuario advinhe qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar 
a possibilidade para o usuario digitar apenas uma letra.
- Quando o usuário digitar apenas uma letra, você
vai conferirse a letra digitada esta napalavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra sereta; exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'python'
letras_usuario = ''
palavra_usuario = ''
tentativas = 0

while True:
    
    letra = input('Digite uma letra:') 
    tentativas += 1
    
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra in palavra_secreta:
        letras_usuario += letra


    palavra_usuario = ''
    for i in palavra_secreta:
        if i in letras_usuario:
            #print(i)
            palavra_usuario += i
        else:
            #print('*')
            palavra_usuario += '*'

    #print(letras_usuario)
    print(palavra_usuario)

    if palavra_usuario == palavra_secreta:
        os.system('cls')
        print('Parabéns! Você acertou!')
        print('Tentativas:', tentativas)
        letras_usuario = ''
        palavra_usuario = ''
        tentativas = 0
        #break



