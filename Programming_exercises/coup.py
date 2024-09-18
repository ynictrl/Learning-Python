# check number of players
# 3 to 10
def check(amount_player):
    amount_cards = 0

    if amount_player == 3:
        amount_cards = 10
    elif amount_player >= 4 and amount_player < 6:
        amount_cards = 15
    elif amount_player >= 6 and amount_player < 9:
        amount_cards = 20
    elif amount_player >= 9 and amount_player < 11:
        amount_cards = 25
    else:
        amount_cards = 0

    rest_cards = amount_cards - amount_player*2

    return amount_cards

print(check(4))

import random
# random - número entre 0 e 1
# numero_0a100 = random.randrange(0, 100, 5)
# print(numero_0a100)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(random.sample(numeros, k=14))
# random.shuffle(numeros)

# randomized cards 
def randomizer(amount_cards, amount_player):
    # ass, cap, con, duq, emb 
    player = ['ass', 'cap', 'con', 'duq', 'emb']
    p = []

    if(amount_cards == 10):
        player*=2
    if(amount_cards == 15):
        player*=3
    if(amount_cards == 20):
        player*=4
    if(amount_cards == 25):
        player*=5

    player = random.sample(player, k=len(player))

    for i in range(amount_player+1): # + rest
        i1 = i*2
        i2 = i1 + 2
        if(i < amount_player):
            p.append(player[i1:i2])
        else:
            p.append(player[i1:])

    return player, p

print(randomizer(check(4), 4))
    

