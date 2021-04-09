# Importing modules

import random
import sys

# Listing all card characteristics

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Creating classes

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]   
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):

        self.all_cards = []

        x = 0
        y = 0

        while x < len(suits):

            while y < len(ranks):
        
                self.all_cards.append(Card(suits[x],ranks[y]))
                y += 1
    
            y = 0
            x += 1

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        self.card = self.all_cards.pop(0)
        return self.card

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self,card):
        if type(card) == list:
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)

    def remove_cards(self, card):
        self.all_cards.pop(0)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards"

# Creating functions

# Function to check if a player won

def check_win(player):
    
    sum = 0

    for card in player.all_cards:
        sum += card.value
    
    if sum == 21:
        print(f"{player.name} won!")
        sys.exit()
    elif sum > 21:
        print(f"{player.name} busted!")
        sys.exit()
    
# Function to compare players' hands and tell the result of the match

def compare_hands(player1, dealer):
    
    sum1 = 0
    sum2 = 0

    for card in player1.all_cards:
        sum1 += card.value
    
    for card in dealer.all_cards:
        sum2 += card.value
    
    if sum1 > sum2:
        print(f"{player1.name} won!")
    elif sum2 > sum1:
        print(f"{dealer.name} won!")
    elif sum1 == sum2:
        print("No one won!")

# Function to show the player cards to the user

def print_cards(player):
    
    print(player)
    
    for card in player.all_cards:
        print(card)

    print("")


# Start of the game logic:

# Interface

print("")

print("Let's begin the game!")

print("")

# Creating Deck

new_deck = Deck()

new_deck.shuffle()

# Creating player1 and dealing 2 first cards

player1_name = input("Insert your name: ")

print("")

player1 = Player(player1_name)

p1_first_cards = [new_deck.deal(), new_deck.deal()]

player1.add_cards(p1_first_cards)

# Creating dealer and dealing 2 first cards

dealer = Player('Dealer')

d_first_cards = [new_deck.deal(), new_deck.deal()]

dealer.add_cards(d_first_cards)

# Showing amount and player 1 cards

print_cards(player1)

# Showing amount and dealer 1 cards

print(dealer)

for card in dealer.all_cards:
    if card == dealer.all_cards[-1]:
        print("Card hidden")
    else:
        print(card)

print("")

# Checking win of both players

check_win(player1)
check_win(dealer)

# Defining variables to be used on while looping

choice = 1

# Player 1 hit or stay loop

while choice == 1:

    print(f"{player1.name}'s turn")

    while True:
        try:
            choice = int(input("Hit - Press 1\nStay - Press 2\n=> "))
        except ValueError:
            print("Insert a valid digit")
        else:
            break

    if choice == 1:
        player1.add_cards(new_deck.deal())
        print_cards(player1)

    check_win(player1)

# Revealing all cards of the dealer

print_cards(dealer)

choice = 1

# Dealer hit or stay loop

while choice == 1:

    print(f"{dealer.name}'s turn")

    while True:
        try:
            choice = int(input("Hit - Press 1\nStay - Press 2\n=> "))
        except ValueError:
            print("Insert a valid digit")
        else:
            break

    if choice == 1:
        dealer.add_cards(new_deck.deal())
        print_cards(dealer)

    check_win(dealer)

compare_hands(player1, dealer)

# Finish