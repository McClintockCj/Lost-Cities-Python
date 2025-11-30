from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit
import random

class deck():
    def __init__(self, deck_cards = []):
        self.deck_cards = deck_cards
        self.full_deck = deck_cards.copy()

    def draw_card(self):
        if self.deck_cards:
            return self.deck_cards.pop()
        else:
            return False

    def new_deck(self):
        self.deck_cards.clear()
        self.full_deck.clear()
        for suit in Suit:
            for _ in range(3):
                temp_card1 = card(suit, 'Wager', Position.DECK)
                self.deck_cards.append(temp_card1)
            for number in range(2, 11):
                temp_card2 = card(suit, number, Position.DECK)
                self.deck_cards.append(temp_card2)

        random.shuffle(self.deck_cards)
        self.full_deck = self.deck_cards.copy()

    def check_end(self):
        if not self.deck_cards:
            return False
        else:
            return True
    
    def print_deck(self, parameter, index = 0):
        loc_x = 101
        
        if index == 7:
            loc_y = 3
        else:
            loc_y = 1

        if len(self.deck_cards) >= 10:
            parameter.addstr(loc_y, loc_x, " --------------- ")
            parameter.addstr(loc_y + 1, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|||             |")
            parameter.addstr(loc_y + 3, loc_x, "|||             |")
            parameter.addstr(loc_y + 4, loc_x, f"|||    {len(self.deck_cards)}/{len(self.full_deck)}    |")
            parameter.addstr(loc_y + 5, loc_x, "|||             |")
            parameter.addstr(loc_y + 6, loc_x, "|||             |")
            parameter.addstr(loc_y + 7, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " --------------- ")
        elif len(self.deck_cards) >= 3:
            parameter.addstr(loc_y, loc_x, " --------------- ")
            parameter.addstr(loc_y + 1, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|||             |")
            parameter.addstr(loc_y + 3, loc_x, "|||             |")
            parameter.addstr(loc_y + 4, loc_x, f"|||     {len(self.deck_cards)}/{len(self.full_deck)}     |")
            parameter.addstr(loc_y + 5, loc_x, "|||             |")
            parameter.addstr(loc_y + 6, loc_x, "|||             |")
            parameter.addstr(loc_y + 7, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " --------------- ")
        elif len(self.deck_cards) == 2:
            parameter.addstr(loc_y, loc_x, " -------------- ")
            parameter.addstr(loc_y + 1, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "||             |")
            parameter.addstr(loc_y + 3, loc_x, "||             |")
            parameter.addstr(loc_y + 4, loc_x, f"||     {len(self.deck_cards)}/{len(self.full_deck)}     |")
            parameter.addstr(loc_y + 5, loc_x, "||             |")
            parameter.addstr(loc_y + 6, loc_x, "||             |")
            parameter.addstr(loc_y + 7, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " -------------- ")
        elif len(self.deck_cards) >= 1:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, f"|     {len(self.deck_cards)}/{len(self.full_deck)}     |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 7, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " ------------- ")
        
