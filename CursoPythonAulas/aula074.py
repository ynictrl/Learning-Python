# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

# def multiplicar(a, b):
#     res = a * b
#     return res

# def duplicar(c):
#     res = multiplicar(c, 2)
#     return res

# def triplicar(c):
#     res = multiplicar(c, 3)
#     return res

# def quaduplicar(c):
#     res = multiplicar(c, 4)
#     return res
    
####

def crair_multiplicador(mult):
    def multiplicar(num):
        return num * mult
    return multiplicar

duplicar = crair_multiplicador(2)
triplicar = crair_multiplicador(3)
quaduplicar = crair_multiplicador(4)

print(duplicar(4), triplicar(5), quaduplicar(3))