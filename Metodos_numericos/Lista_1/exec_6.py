A, B, C, D, E, F = 10, 11, 12, 13, 14, 15

# BASE 2 PARA BASE 16

bin_input = '1011010011'
bin = ''
res_b16 = ''

# adptar casas inteiras (acrescentar zeros a esquerda se necessario)
if len(bin_input)%4 == 3:
    bin += '0'
    bin += bin_input
elif len(bin_input)%4 == 2:
    bin += '00'
    bin += bin_input
elif len(bin_input)%4 == 1:
    bin += '000'
    bin += bin_input
else:
    bin += bin_input

print(bin) # numero adaptado

piece_bin = ''
piece_res = 0
for i in bin:
    piece_bin += i 

    if len(piece_bin) == 4:
        print(piece_bin) # parte separada
        j = len(piece_bin) - 1  # iteravel de trás pra frente
        int_exp = -1 # expoente
        piece_res = 0 # resultado piece

        while j >= 0:
            int_exp += 1 # acréscimo do expoente
            if piece_bin[j] != '0': piece_res += 2**(int_exp) # resltado recebe apenas para '1'
            j -= 1 # decremento
            
        if piece_res > 9:
            word = 'ABCDEF'
            for i in range(6):
                if piece_res == (i + 10):
                    piece_res = word[i]
        
        res_b16 += str(piece_res) # acrescimo no resultado
        piece_bin = '' # resetar parte

print(res_b16)