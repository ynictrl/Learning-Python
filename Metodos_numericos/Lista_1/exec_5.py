# BASE 2 PARA BASE 8

bin_input = '1001001110011010'
bin = ''
res_b8 = ''

# adptar casas inteiras (acrescentar zeros a esquerda se necessario)
if len(bin_input)%3 == 2:
    bin += '0'
    bin += bin_input
elif len(bin_input)%3 == 1:
    bin += '00'
    bin += bin_input
else:
    bin += bin_input

print(bin) # numero adaptado

piece_bin = ''
piece_res = 0
for i in bin:
    piece_bin += i 

    if len(piece_bin) == 3:
        print(piece_bin) # parte separada
        j = len(piece_bin) - 1  # iteravel de trás pra frente
        int_exp = -1 # expoente
        piece_res = 0 # resultado piece

        while j >= 0:
            int_exp += 1 # acréscimo do expoente
            if piece_bin[j] != '0': piece_res += 2**(int_exp) # resltado recebe apenas para '1'
            j -= 1 # decremento
            
        res_b8 += str(piece_res) # acrescimo no resultado
        piece_bin = '' # resetar parte

print(res_b8)

print(f'\n-----------------------------\n')

# BASE 8 PARA BASE 2

b8 = '246'
res_bin = []
res_bin_value = ''

i = len(b8) - 1
while i > -1:
    # i == 6,4,2
    div = int(b8[i])
    print(b8[i])
    
    while div >= 1:
        res_bin += str(div % 2)

        div_succ = div // 2
        div = div_succ

    if int(b8[i]) > 1 and int(b8[i]) < 4: res_bin += '0'# 0 1 (10 11) 100...111
    if int(b8[i]) < 2: # (0 1) 10 11 100...111
        res_bin += '0' 
        res_bin += '0'

    print(res_bin, '..')
    i -= 1

print(res_bin)
res_bin.reverse()
print(res_bin)

for j in res_bin:
    res_bin_value += j

print(res_bin_value)