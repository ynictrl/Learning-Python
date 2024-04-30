# i_i = 1 # incdice inicial
# i_f = 4 # indice final
# sum = 2 # termo somatorio
# res = 0 # resultado

def somatorio(i_i, i_f, sum):
    res = 0
    while i_i <= i_f:
        res += i_i*sum
        i_i += 1
    return res

soma1 = 8.000 - somatorio(1, 10000, 0.008)

soma2 = 10.000 - somatorio(1, 8000, 0.0125)

print(soma1, soma2)

    

        


