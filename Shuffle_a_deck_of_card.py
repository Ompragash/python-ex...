#Python program to shuffle a deck of card


import itertools, random

#MAke a deck of cards
deck = list(itertools.product(range(1, 14),['Spade', 'Heart', 'Diamond', 'Club']))


#Shuffle the cards
random.shuffle(deck)

print("You get: ")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])


