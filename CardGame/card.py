'''
'''
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}  

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop() if self.hand else None

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards."
    

new_deck = Deck()
'''
for card in new_deck.cards:
    print(card)
'''
new_deck.shuffle()
print("\nShuffled Deck:")
'''
for card in new_deck.cards:
    print(card)
'''

player1 = Player("Alice")
player2 = Player("Bob")
for _ in range(26):
    player1.add_card(new_deck.deal_one())
    player2.add_card(new_deck.deal_one())

print(player1)
print(player2)

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"\nRound {round_num}:")
    
    card1 = player1.play_card()
    card2 = player2.play_card()
    
    if not card1 or not card2:
        game_on = False
        break
    
    print(f"{player1.name} plays: {card1}")
    print(f"{player2.name} plays: {card2}")
    
    if card1.value > card2.value:
        player1.add_card(card1)
        player1.add_card(card2)
        print(f"{player1.name} wins the round.")
    elif card1.value < card2.value:
        player2.add_card(card1)
        player2.add_card(card2)
        print(f"{player2.name} wins the round.")
    else:
        print("It's a tie! No cards are won this round.")

    if not player1.hand:
        print(f"{player1.name} has no more cards. {player2.name} wins the game!")
        game_on = False
    elif not player2.hand:
        print(f"{player2.name} has no more cards. {player1.name} wins the game!")
        game_on = False
print(player1)
print(player2)
