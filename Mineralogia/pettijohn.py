# Diagrma de Pettijohn

# Q  - Quartzo com exceção de chert
# F  - Fieldspato (Fragmentos de Granito + Fragmentos de Gnaisse)
# FR - Fragmento lítico
# M  - Matriz

def Aproximar(a):
    if (a-int(a)) >= 0.5:
        a = int(a) + 1
    else:
        a = int(a)
    
    return a

def Normalizar(q, f, fr, m):
    total = q + f + fr
    q_n  = q  * 100/total
    f_n  = f  * 100/total
    fr_n = fr * 100/total

    # aproximação
    q_n = Aproximar(q_n)
    f_n = Aproximar(f_n)
    fr_n = Aproximar(fr_n)

    porcentagem = f'Q: {q_n}%, F: {f_n}%, FR: {fr_n}%'

    if m <= 15:
        return porcentagem, Diagrama_15(q_n, f_n, fr_n)
    return porcentagem, Diagrama_15_75(q_n, f_n, fr_n)
    

# Matriz <15%
# Q - <50% (arcóseo, arcóseo lítico, litoarenito)
# Q - >50% e <90% (arcóseo, arcóseo lítico, litoarenito, subárcósio, sublitoarenito)
# Q - >90% (subárcósio, sublitoarenito, quartzo-arenito)

# F - <5% (litoarenito, sublitoarenito, quartzo-arenito)
# F - >5% e <25% (litoarenito, sublitoarenito, subárcósio)
# F - >25% e <50% (litoarenito, arcóseo, arcóseo lítico)
# F - >50% e <75% (arcóseo, arcóseo lítico)
# F - >75% (arcóseo)

# FR - <5% (quartzo-arenito, subárcósio, arcóseo)
# FR - >5% e <10% (sublitoarenito, subárcósio, arcóseo)
# FR - >10% e <25% (sublitoarenito, subárcósio, arcóseo lítico, arcóseo)
# FR - >25% e <50% (litoarenito, arcóseo lítico)
# FR - >50% (litoarenito)

def Diagrama_15(q_n, f_n, fr_n):

    # DIAGRAMA
    if q_n <= 50:
        q_pos = ['arcóseo', 'arcóseo lítico', 'litoarenito']
    elif (q_n > 50) and (q_n <= 90):
        q_pos = ['arcóseo', 'arcóseo lítico', 'litoarenito', 'subárcósio', 'sublitoarenito']
    else:# > 90
        q_pos = ['subárcósio', 'sublitoarenito', 'quartzo-arenito']

    if f_n <= 5:
        f_pos = ['litoarenito', 'sublitoarenito', 'quartzo-arenito']
    elif (f_n > 5) and (f_n <= 25):
        f_pos = ['litoarenito', 'sublitoarenito', 'subárcósio']
    elif (f_n > 25) and (f_n <= 50):
        f_pos = ['litoarenito', 'arcóseo', 'arcóseo lítico']
    elif (f_n > 50) and (f_n <= 75):
        f_pos = ['arcóseo', 'arcóseo lítico']
    else:# > 75
        f_pos = ['arcóseo']

    if fr_n <= 5:
        fr_pos = ['quartzo-arenito', 'subárcósio', 'arcóseo']
    elif (fr_n > 5) and (fr_n <= 10):
        fr_pos = ['sublitoarenito', 'subárcósio', 'arcóseo']
    elif (fr_n > 10) and (fr_n <= 25):
        fr_pos = ['sublitoarenito', 'subárcósio', 'arcóseo lítico', 'arcóseo']
    elif (fr_n > 25) and (fr_n <= 50):
        fr_pos = ['litoarenito', 'arcóseo lítico']
    else:# > 50
        fr_pos = ['litoarenito']

    total = q_pos + f_pos + fr_pos

    return intersecao(total)


def Diagrama_15_75(q_n, f_n, fr_n):

    # DIAGRAMA
    if q_n <= 90:
        q_pos = ['grauvaca feldspática', 'grauvaca lítica']
    elif (q_n > 90) and (q_n <= 95):
        q_pos = ['grauvaca feldspática', 'grauvaca lítica', 'quartzo-grauvaca']
    else:# > 95
        q_pos = ['quartzo-grauvaca']

    if f_n <= 5:
        f_pos = ['grauvaca lítica', 'quartzo-grauvaca']
    elif (f_n > 5) and (f_n <= 50):
        f_pos = ['grauvaca lítica', 'grauvaca feldspática']
    else:# > 50
        f_pos = ['grauvaca feldspática']

    if fr_n <= 5:
        fr_pos = ['quartzo-grauvaca', 'grauvaca feldspática']
    elif (fr_n > 5) and (fr_n <= 50):
        fr_pos = ['grauvaca lítica', 'grauvaca feldspática']
    else:# > 50
        fr_pos = ['grauvaca lítica']

    total = q_pos + f_pos + fr_pos

    return intersecao(total)


def intersecao(l):
    for i in l:
        count = 0
        for j in l:
            if i == j:
                count += 1

        if count == 3:
            classificacao = i
            break

    return classificacao

print(Normalizar(90,  0,  0, 10))
print(Normalizar(35, 22, 31, 12))
print(Normalizar(10, 48, 38,  5))
print(Normalizar(77, 14,  5,  4))
print(Normalizar(85, 15,  0,  0))
print(Normalizar(54, 22, 13, 11))
print(Normalizar(42, 38,  4, 16))
print(Normalizar(78,  5, 15,  3))
print(Normalizar(18,  9, 61, 12))
print(Normalizar(16, 39, 24, 21))
print(Normalizar( 9,  9, 69, 14))
print(Normalizar( 0,  0, 94,  6))
print(Normalizar(93,  2,  2,  3))
print(Normalizar( 9, 79,  5,  7))
print(Normalizar(76,  2,  2, 21))
print(Normalizar(38, 11, 27, 24))
print(Normalizar(79,  0,  0, 21))
print(Normalizar( 0, 94,  0,  6))
print(Normalizar(84,  0,  9,  7))
print(Normalizar( 9, 32, 50, 10))


