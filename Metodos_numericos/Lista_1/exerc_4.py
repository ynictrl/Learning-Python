numeros = [-3, 0, 5, 12, -3, 5, 0, -1] # 2 zeros, 3 pos, 3 neg
count = [0, 0, 0] # [0] == neg, [1] == zero, [2] == pos

for i in numeros:
    if i < 0: 
        count[0] += 1
    if i == 0: 
        count[1] += 1
    if i > 0: 
        count[2] += 1

print(f'Os números listados possuem:\n'
      f'{count[0]} números negativos\n'
      f'{count[1]} números zeros\n'
      f'{count[2]} números positivos\n')
    