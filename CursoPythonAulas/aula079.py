# Sets - Conjuntos em Python (tipo set)
# São mutáveis, porém aceitam apenas tipos imutáveis 
# como valor interno

# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set('Nicolas')
s1 = set() # vázio
s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientespara remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - Não tem índices;
# - Não garentem ordem;
# - São iteráveis (for, in, not in);

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Nicolas')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
# s1.discard('Olá mundo')
# s1.discard('Nicolas')
# print(s1)


# Operadores úteis:
# união | união (union) : Une
# intersecção & (intersection) : Itens presentes em ambos
# diferença - : Itens presentes apenas no set no primeiro termo
# diferença simétrica ^ : Itens que não estão em ambos

# s1 = set((1, 2, 3))
# s2 = set((2, 3, 4))
# s3 = s1 | s2 # união
# s4 = s1 & s2 # intersection
# s5 = s1 - s2 # diferença
# s6 = s2 - s1 # diferença
# s7 = s1 ^ s2 # diferença simétrica

# print(f'união: {s3}\ninterceção: {s4}\ndiferença_s1: {s5}\ndiferença_s2: {s6}\ndiferença simétrica: {s7}')


# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'f' in letras:
        print('Parabéns')
        break

    print(letras)

