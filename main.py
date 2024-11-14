from cards import Card

import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
ranks = ("Two", "Three","Four","Five","Six","Seven","Eight","Nine","Ten", "Jack", "Queen", "King", "Ace")

print("Testing the Card Class")

card1 = Card(suits[2],ranks[4])
#Test the get functions
if card1.get_suit() == suits[2]:
    print("Passed suit test")
if card1.get_rank() == ranks[4]:
    print("Passed rank test")
if card1.get_value() == 6:
    print("Passed value test")

print(card1)#This should print the card from the __str__ method

card2 = Card(suits[0],ranks[12])
#Test the get functions
if card1.get_suit() == suits[0]:
    print("Passed suit test")
if card1.get_rank() == ranks[12]:
    print("Passed rank test")
if card1.get_value() == 11:
    print("Passed value test")

print(card2)#This should print the card from the __str__ method

card3 = Card(suits[3],ranks[11])
#Test the get functions
if card1.get_suit() == suits[3]:
    print("Passed suit test")
if card1.get_rank() == ranks[11]:
    print("Passed rank test")
if card1.get_value() == 10:
    print("Passed value test")

print(card3)#This should print the card from the __str__ method

#create all 52 unique cards. Hint, use the tuples ranks and suits with some for loops, and store them in a list.
deck = [] #create a list to store the cards
for s in suits:
    for r in ranks:
        deck.append(Card(s,r))

#print the cards to see them
for c in deck:
    print(c) # c  is a card in the deck, each time this loop repeats then it will call the __str__ method from the Card class
    
    
