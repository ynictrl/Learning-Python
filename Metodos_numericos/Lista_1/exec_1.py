
def conversion(numBin):
    
    numBin = numBin.split(".") # dividir em as partes 

    # CASA INTEIRA
    i = len(numBin[0]) - 1  # iteravel de trás pra frente
    int_exp = -1 # expoente
    int_res = 0 # resultado final

    while i >= 0:
        int_exp += 1 # acréscimo do expoente
        if numBin[0][i] != '0': int_res += 2**(int_exp) # resltado recebe apenas para '1'
        i -= 1 # decremento

    # ---------------------------------------------------------

    # CASA DECIMAL
    j = -(len(numBin[1])) # iteravel de trás pra frente
    float_exp = 0 # expoente
    float_res = 0 # resultado final 

    while j < 0:
        float_exp -= 1 # decréscimo do expoente
        if numBin[1][j] != '0': float_res += 2**(float_exp) # resltado recebe apenas para '1'
        j += 1 # acréscimo

    res = int_res + float_res # soma dos resultados
    return res

print(conversion('11.11110101'))
print(conversion('10110101.1010101'))