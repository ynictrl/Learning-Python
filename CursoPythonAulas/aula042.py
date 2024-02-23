frase = 'O Python é uma linguagem de programaçã0 ' \
'multiparadigma. Python foi criado por Guido van Rossum'

i = 0 
word_max = ''
word_max_count = 0

while i < len(frase):
    word_current = frase[i]

    if word_current == ' ':
        i += 1
        continue

    word_current_count = frase.count(word_current)

    if word_max_count < word_current_count:
        word_max_count = word_current_count
        word_max = word_current

    print(word_max)
    i += 1

print(f'A letra, {word_max}, apareceu mais vezes sendo, {word_max_count}')

