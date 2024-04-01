# valores fornecidos pelo usuário
n1, n2, n3 = 12, 12, 14

def maior_valor(a, b, c):
    if a > b and a > c:
        return f'A {a} é o maior valor!'
    if b > a and b > c:
        return f'B {b} é o maior valor!'
    if c > a and c > b:
        return f'C {c} é o maior valor!'
    
    return '2 ou mais valores são iguais!'
    
print(maior_valor(n1, n2, n3))