"""
Tipo tupla - Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz' # ou ('Maria', 'Helena', 'Luiz)
print(nomes[1])
print(nomes, type(nomes))

nomes2 = ['Carlos', 'Sergio', 'Joca'] # list
nomes2 = tuple(nomes2) # converção
print(nomes[2])
print(nomes2, type(nomes2))
