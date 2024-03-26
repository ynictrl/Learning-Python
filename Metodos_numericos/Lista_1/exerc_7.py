n = 5
asteriscos_for = ''
asteriscos_while = ''

for i in range(n):
    asteriscos_for += '*'

j = 0
while j < n:
    asteriscos_while += '*'
    j += 1

print(f'for:{asteriscos_for} | while:{asteriscos_while}')