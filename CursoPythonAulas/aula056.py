"""
split e join com list e str
split - divite com string
join - une uma string
strip - corta os espaços
"""

frase = 'Olha só, que coisa interessante'
lista_frases = frase.split(', ') # separa a string para uma lista
print(lista_frases)

frase = '   Olha só     ,  que coisa interessante   '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip)
    #print(lista_frases[i].strip()) # strip - corta os espaços, rstrip(right), lstrip(left)

print(lista_frases_cruas)
print(lista_frases)

######
#join

frases_unidas = '-'.join('AINDA')
print(frases_unidas)

frases_unidas2 = '//'.join(lista_frases_cruas) # somente iterável
print(frases_unidas2)