"""

"""
salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0       
    ['Elaine'], # 1
    # 0       1        2
    ['João', 'Paulo', 'Guilherme'], # 2

    #['Pedro', [0, 1, 2]], # 3
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
#print(salas[3][1][2])

for sala in salas:
    print(sala)
    for alunos in sala:
        print(alunos)