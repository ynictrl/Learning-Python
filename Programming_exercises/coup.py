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

    return amount_cards, rest_cards

print(check(4))