# 6 -- [0, 1, 1, 2, 3, 5]

def fibonnaci(num):
    if num < 0: return 'O número não pode ser negativo' # rise Exeption

    if num == 0: return []

    curr = 1
    sequence = [0]

    if num > 1:
        for i in range(num-1):
            sequence.append(curr)
            if i > 0: curr = sequence[i] + sequence[i+1]
    
    # print(sequence)
    return sequence

print(fibonnaci(6))

# lista = []
# curr = 1

# for i in range(15):
#     lista.append(curr)
#     if i > 0: curr = lista[i-1] + lista[i]
#     print(lista)