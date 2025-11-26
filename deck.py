from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit
import random

class deck():
    def __init__(self, deck_cards = []):
        self.deck_cards = deck_cards

    def draw_card(self):
        if self.deck_cards:
            return self.deck_cards.pop()
        else:
            return False

    def new_deck(self):
        for suit in Suit:
            for _ in range(3):
                temp_card1 = card(suit, 'Wager', Position.DECK)
                self.deck_cards.append(temp_card1)
            for number in range(2, 11):
                temp_card2 = card(suit, number, Position.DECK)
                self.deck_cards.append(temp_card2)

        random.shuffle(self.deck_cards)