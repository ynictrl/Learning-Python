"""
Faça uma lista de compra com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os
lista = []

while True:
    #os.system('cls')
    acao = input('O que deseja? [i]nserir, [a]pagar ou [l]istar')
    os.system('cls')

    if acao == 'i':
        novo_elemento = input('Digite o que deseja inserir na lista:')
        lista.append(novo_elemento)

    elif acao == 'a':
        if len(lista) > 0: # lista não vazia
            indice_del = input('Qual item deseja remover?')
            try:
                del lista[int(indice_del)]
            except ValueError:
                print('Termo inválido! Digite um número inteiro')
            except IndexError:
                print('Termo inválido! Digite um número que seja um index na lista')
            except Exception:
                print('Erro desconhecido!')
        else:
            print('A lista está vázia!')
    
    elif acao == 'l':
        if len(lista) > 0: # lista não vazia
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('A lista está vázia!')

    else:
        print('Termo inválido!')

    continue
