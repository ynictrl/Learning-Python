# BASE 2 PARA BASE 16

bin_input = input('Digite um número na base 2: ')
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

# print(bin) # numero adaptado

piece_bin = ''
piece_res = 0
for i in bin:
    piece_bin += i 

    if len(piece_bin) == 4:
        # print(piece_bin) # parte separada
        j = len(piece_bin) - 1  # iteravel de trás pra frente
        int_exp = -1 # expoente
        piece_res = 0 # resultado piece

        while j >= 0:
            int_exp += 1 # acréscimo do expoente
            if piece_bin[j] != '0': piece_res += 2**(int_exp) # resltado recebe apenas para '1'
            j -= 1 # decremento
            
        if piece_res > 9:
            word = 'ABCDEF'
            for k in range(6):
                if piece_res == (k + 10):
                    piece_res = word[k]
        
        res_b16 += str(piece_res) # acrescimo no resultado
        piece_bin = '' # resetar parte

print(f'({bin_input})b2 = ({res_b16})b16')

print(f'\n-----------------------------\n')

# BASE 16 PARA BASE 2

b16 = input('Digite um número na base 16: ') #D3
res_bin = []
res_bin_value = ''
num =0

i = len(b16) - 1
while i > -1:

    #if int(b16[i]) > 9:
    word = 'ABCDEF'
    if b16[i] in word:
        for j in range(6):
            if b16[i] == word[j]:
                div = 10 + j
                num = div
    else:
        div = int(b16[i])
        num = div

    # print(b16[i])
    
    while div >= 1:
        res_bin += str(div % 2)

        div_succ = div // 2
        div = div_succ

    if num > 3 and num < 8: # 0 1 10 11 (100 101 110 111)
        res_bin += '0'
    if num > 1 and num < 4: # 0 1 (10 11) 100...111
        res_bin += '0'
        res_bin += '0'
    if num < 2: # (0 1) 10 11 100...111
        res_bin += '0' 
        res_bin += '0'
        res_bin += '0'

    # print(res_bin, '..')
    i -= 1

# print(res_bin)
res_bin.reverse()
# print(res_bin)

for j in res_bin:
    res_bin_value += j

print(f'({b16})b16 = ({res_bin_value})b2')
