import random

cards = ["Jack", "Queen", "King"]

# shuffles the list in place
random.shuffle(cards)

for card in cards:
    print(card)