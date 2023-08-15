# Write your blackjack game here.

import random
import math

# class for an individual card
class Card:
    def __init__(self, suit, value):
        # initiate, gets called when create new instance of class
        # attributes
        self.suit = suit
        self.value = value
        

# class for the deck of cards
class Deck:
    def __init__(self):
        self.card_deck = []
        suits = ['♠', '♥', '♦', '♣']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.card_deck.append(card)
        
    def __str__(self):

        card_strings = [f"{card.value}{card.suit}" for card in self.card_deck]
        return ', '.join(card_strings)  # Join the card strings with commas

        # 52 cards in random order
        # create 52 cards, then short
    def shuffle(self):
        random.shuffle(self.card_deck)
        return self.card_deck


        # self.order = 'something'

# class for the automated dealer
# Dealer or Player could be child of the other (Dealer child of Player)
class Dealer:
    def __init__(self):
        # attributes
        self.hand_value = 0

        # methods
            # get 2 cards
            # calculate value of hand
            # "hit to get another card if value < 17"

class Player:
    def __init__(self, name='Nathan'):
    # attributes
        # Initialize an empty list to store cards
        self.cards = [] 
        if name is None:
            self.name = input('What is your name? ')
        else:
            self.name = name

    #methods
    def __str__(self):
        return self.name

    def get_card(self, deck):
        # Remove top card from deck
        top_card = deck.card_deck.pop()
        # Add the card to the player's cards list
        self.cards.append(top_card)

            # get 2 cards
            # calculate value of hand
            # prompt user to "hit" if they want
    def hit(self, deck):
        hit = input('Would you like to hit? [y/n]: ')
        if hit.lower() == 'y':
            self.get_card(deck)
            if self.hand_value > 21:
                print(f'Your hand value is now {self.hand_value}. You bust. Better luck next hand.')
            else:
                print(f''' you got a {self.cards[-1].value} of {self.cards[-1].suit}
The total hand value is {self.hand_value}''')
                return self.hit(deck)
        else:
            print(f'You chose to stay. Your hand value is {self.hand_value}')
            
    
    @property
    def hand_value(self):
        total = 0
        aces_count = 0
        for card in self.cards:
            face_cards = ['J', 'Q', 'K']
            if card.value in face_cards:
                total += 10
            elif card.value == 'A':
                if (total + 11) > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += int(card.value)
        
        # Check if hand is busted with Aces counting as 11, then reduce them to 1
        while total > 21 and aces_count:
            total -= 10
            aces_count -= 1
        
        return total

# Make a subclass of player for the dealer. 
# The dealer hits automatically when value < 17.
class Dealer(Player):
    def hit(self, deck):
        if self.hand_value < 17:
            self.get_card(deck)
            
            if self.hand_value > 21:
                print(f'The dealer got a {self.cards[-1].value} of {self.cards[-1].suit}')
                print(f'The dealer\'s hand value is now {self.hand_value}. The dealer busts.')
            else:
                print(f''' The dealer got a {self.cards[-1].value} of {self.cards[-1].suit}
The dealer's hand value is {self.hand_value}''')
                return self.hit(deck)
        else:
            print(f'The dealer chose to stay. The dealer\'s hand value is {self.hand_value}')

class Game:
    def __init__(self):
        # attributes
            # name of game
            # game over?
            self.name = 'Blackjack'
            self.game_over = False
            
        # methods
            # display player cards (2nd card and those after)

    def __str__(self):
        return self.name
    
    def game_intro(self):
        # introduce player to blackjack
        print(f'''{self.player}, welcome to {self.name}. 
You got a {self.player.cards[0].value} of {self.player.cards[0].suit} 
and a {self.player.cards[1].value} of {self.player.cards[1].suit}
The total hand value is {self.player.hand_value}''')
            
        print(f'''The dealer\'s faceup card is a {self.dealer.cards[1].value} of {self.dealer.cards[1].suit}''')
        print(f'The dealer\'s hidden card is a {self.dealer.cards[0].value} of {self.dealer.cards[0].suit}')

    def start_game(self):
        # create instances of player and dealer
        self.player = Player()
        self.dealer = Dealer()

        # create instance of the deck and then shuffle
        self.deck = Deck()
        self.deck.shuffle()

        # print the shuffled deck
        print(self.deck)

        # give player and dealer 2 cards 
        # order: player, dealer, player, dealer
        self.player.get_card(self.deck)
        self.dealer.get_card(self.deck)
        self.player.get_card(self.deck)
        self.dealer.get_card(self.deck)

        # introduce player to blackjack
        self.game_intro()

        # give option for dealer and player to hit
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)

        
        
        
        
    # def play_game(self):


new_game = Game()
new_game.start_game()