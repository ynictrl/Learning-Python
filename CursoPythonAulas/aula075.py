# Dicionários em Phyton (tipo dict)
# Dicionáriod são estruturas de dados do tipo
# par de "chave" e "valor"
# Chaves podem ser consideras como o "índice"
# que vimos na lista e podem ser de qualquer tipo, incluindo outro
# dicionário.
# usamos as chaves - {} - ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, truple
# Mutáveis: dict, list

pessoa = {
    'nome': 'Nicolas',
    'sobrenome': 'Gomes',
    'idade': '19',
    'altura': '1.80',
    'endereços': [
        {'rua': 'inferno', 'número': '666'},
        {'rua': 'paraido', 'número': '777'},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')