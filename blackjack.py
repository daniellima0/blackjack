import random
import sys

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

def check_win(player):
    
    sum = 0

    for card in player.all_cards:
        sum += card.value
    
    if sum == 21:
        print(f"{player.name} ganhou!")
        sys.exit()
    elif sum > 21:
        print(f"{player.name} deu bust!")
        sys.exit()
    
def compare_hands(player1, dealer):
    
    sum1 = 0
    sum2 = 0

    for card in player1.all_cards:
        sum1 += card.value
    
    for card in dealer.all_cards:
        sum2 += card.value
    
    if sum1 > sum2:
        print(f"{player1.name} ganhou!")
    elif sum2 > sum1:
        print(f"{dealer.name} ganhou!")
    elif sum1 == sum2:
        print("Ninguém ganhou!")

def print_cards(player):
    
    print(player)
    
    for card in player.all_cards:
        print(card)

    print("")


#Início do lógica do jogo:

# Interface - Início

print("")

print("Let's begin the game!")

print("")

# Criando Deck

new_deck = Deck()

new_deck.shuffle()

# Criando player1 e adicionando 2 primeiras cartas

player1_name = input("Insira seu nome: ")

print("")

player1 = Player(player1_name)

p1_first_cards = [new_deck.deal(), new_deck.deal()]

player1.add_cards(p1_first_cards)

# Criando dealer e adicionando 2 primeiras cartas

dealer = Player('Dealer')

d_first_cards = [new_deck.deal(), new_deck.deal()]

dealer.add_cards(d_first_cards)

# Mostrando número e quais cartas o player 1 tem

print_cards(player1)

# Mostrando número e quais cartas o dealer tem

print(dealer)

for card in dealer.all_cards:
    if card == dealer.all_cards[-1]:
        print("Card down")
    else:
        print(card)

print("")

# Checando vitória dos dois

check_win(player1)
check_win(dealer)

# Definindo variáveis a serem usadas no looping

vez = 1
escolha = 1

# Looping do hit ou stay do jogador 1

while escolha == 1:

    print(f"Vez do {player1.name}")

    while True:
        try:
            escolha = int(input("Hit - Pressione 1\nStay - Pressione 2\n=> "))
        except ValueError:
            print("Pare de ser um mamute e insira um dígito")
        else:
            break

    if escolha == 1:
        player1.add_cards(new_deck.deal())
        print_cards(player1)

    check_win(player1)

# Revelando todas as cartas do dealer

print_cards(dealer)

escolha = 1

# Looping do hit ou stay do dealer

while escolha == 1:

    print(f"Vez do {dealer.name}")

    while True:
        try:
            escolha = int(input("Hit - Pressione 1\nStay - Pressione 2\n=> "))
        except ValueError:
            print("Pare de ser um mamute e insira um dígito")
        else:
            break

    if escolha == 1:
        dealer.add_cards(new_deck.deal())
        print_cards(dealer)

    check_win(dealer)

compare_hands(player1, dealer)

#-----------------------------------------------------------
# Depois trocar tudo para inglês e postar no github!!
# Inclusive trocar o tic tac toe para inglês tbmm!!