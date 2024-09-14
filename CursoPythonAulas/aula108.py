# Exercício - Somar listas
# Considere suas listas A e B
# A = [1, 2, 3, 4, 5, 6]
# B = [1, 2, 3, 4]
# res = [2, 4, 6, 8]

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4]

def soma_lista(l1, l2):
    interval = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(interval)]

print(soma_lista(a, b))

# lista_a = [10, 2, 3, 40, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)