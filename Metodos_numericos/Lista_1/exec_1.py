num = '1110.101' 
numPart = num.split(".")
    
def conversion(lista):
    
    # CASA INTEIRA
    i = len(lista[0]) - 1  # iteravel de trás pra frente
    int_exp = -1 # expoente
    int_res = 0 # resultado final

    while i >= 0:
        int_exp += 1 # acréscimo do expoente
        if lista[0][i] != '0': int_res += 2**(int_exp) # resltado recebe apenas para '1'
        i -= 1 # decremento

    # ---------------------------------------------------------

    # CASA DECIMAL
    j = -(len(lista[1])) # iteravel de trás pra frente
    float_exp = 0 # expoente
    float_res = 0 # resultado final 

    while j < 0:
        float_exp -= 1 # decréscimo do expoente
        if lista[1][j] != '0': float_res += 2**(float_exp) # resltado recebe apenas para '1'
        j += 1 # acréscimo

    res = int_res + float_res # soma dos resultados
    return res

print(conversion(numPart))