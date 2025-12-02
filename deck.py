import curses
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit
import random

class deck():
    def __init__(self, deck_cards = []):
        self.deck_cards = deck_cards
        self.last_card = 0
        self.full_deck = deck_cards.copy()
        self.discard_cards = {Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]}

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
                temp_card1 = card(suit, 0, Position.DECK)
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
            parameter.addstr(loc_y + 4, loc_x, f"|||     {len(self.deck_cards)}/{len(self.full_deck)}    |")
            parameter.addstr(loc_y + 5, loc_x, "|||             |")
            parameter.addstr(loc_y + 6, loc_x, "|||             |")
            parameter.addstr(loc_y + 7, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " --------------- ")
        elif len(self.deck_cards) == 2:
            parameter.addstr(loc_y, loc_x, " -------------- ")
            parameter.addstr(loc_y + 1, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "||             |")
            parameter.addstr(loc_y + 3, loc_x, "||             |")
            parameter.addstr(loc_y + 4, loc_x, f"||     {len(self.deck_cards)}/{len(self.full_deck)}    |")
            parameter.addstr(loc_y + 5, loc_x, "||             |")
            parameter.addstr(loc_y + 6, loc_x, "||             |")
            parameter.addstr(loc_y + 7, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " -------------- ")
        elif len(self.deck_cards) >= 1:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, f"|     {len(self.deck_cards)}/{len(self.full_deck)}    |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 7, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 8, loc_x, " ------------- ")
        

    def discard(self, index, players_cards = None):
        for card in players_cards:
            if card.hand_num == index:
                self.last_card = card
                players_cards.remove(card)
                card.set_position(Position.DISCARD)
                self.discard_cards[card.suit].append(card)

    def print_discard(self, parameter, index = 0):
        cord_x = 5
        cord_y = 1

        color_choice = curses.A_NORMAL
        
        for key in self.discard_cards.keys():
            color_choice = curses.color_pair(key.value)
            if (len(self.discard_cards[key]) > 0):
                if key.value == index:
                    self.discard_cards[key][-1].cardprint(parameter, cord_y + 2, cord_x + (16 * (key.value -1)))

                    if len(self.discard_cards[key]) > 1:
                        for i, card in enumerate(self.discard_cards[key][:-1]):
                            if card.num == 0:
                                parameter.addstr(cord_y + 1, cord_x + (16 * (key.value -1)) + (i*2) + 1, "W|", color_choice | curses.A_UNDERLINE)
                            else:
                                parameter.addstr(cord_y + 1, cord_x + (16 * (key.value -1)) + (i*2) + 1, f"{card.num}|", color_choice | curses.A_UNDERLINE)
                else:
                    self.discard_cards[key][-1].cardprint(parameter, cord_y, cord_x + (16 * (key.value -1)))
            




        # for key in self.discard_cards:
        #     if key == Suit.RED and self.discard_cards[Suit.RED]:
        #         if index == 1 and len(self.discard_cards[Suit.RED]) > 0:
        #             self.discard_cards[Suit.RED][len(self.discard_cards[Suit.RED]) - 1].cardprint(parameter, cord_y + 2, cord_x)
        #         elif (len(self.discard_cards[Suit.RED]) > 0):
        #             self.discard_cards[Suit.RED][len(self.discard_cards[Suit.RED]) - 1].cardprint(parameter, cord_y, cord_x)   
        #         else:
        #             self.discard_cards[Suit.RED][0].cardprint(parameter, cord_y, cord_x)

        #     if key == Suit.GREEN and self.discard_cards[Suit.GREEN]:
        #         if index == 2 and len(self.discard_cards[Suit.GREEN]) > 0:
        #             self.discard_cards[Suit.GREEN][len(self.discard_cards[Suit.GREEN]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16)))
        #         elif (len(self.discard_cards[Suit.GREEN]) > 0):
        #             self.discard_cards[Suit.GREEN][len(self.discard_cards[Suit.GREEN]) - 1].cardprint(parameter, cord_y, (cord_x + (16)))   
        #         else:
        #             self.discard_cards[Suit.GREEN][0].cardprint(parameter, cord_y, cord_x)

        #     if key == Suit.BLUE and self.discard_cards[Suit.BLUE]:
        #         if index == 3 and len(self.discard_cards[Suit.BLUE]) > 0:
        #             self.discard_cards[Suit.BLUE][len(self.discard_cards[Suit.BLUE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 2)))
        #         elif (len(self.discard_cards[Suit.BLUE]) > 0):
        #             self.discard_cards[Suit.BLUE][len(self.discard_cards[Suit.BLUE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 2)))
        #         else:
        #             self.discard_cards[Suit.BLUE][0].cardprint(parameter, cord_y, (cord_x + (16 * 2)))

        #     if key == Suit.YELLOW and self.discard_cards[Suit.YELLOW]:
        #         if index == 4 and len(self.discard_cards[Suit.YELLOW]) > 0:
        #             self.discard_cards[Suit.YELLOW][len(self.discard_cards[Suit.YELLOW]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 3)))
        #         elif (len(self.discard_cards[Suit.YELLOW]) > 0):
        #             self.discard_cards[Suit.YELLOW][len(self.discard_cards[Suit.YELLOW]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 3)))
        #         else:
        #             self.discard_cards[Suit.YELLOW][0].cardprint(parameter, cord_y, (cord_x + (16 * 3)))

        #     if key == Suit.PURPLE and self.discard_cards[Suit.PURPLE]:
        #         if index == 5 and len(self.discard_cards[Suit.PURPLE]) > 0:
        #             self.discard_cards[Suit.PURPLE][len(self.discard_cards[Suit.PURPLE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 4)))
        #         elif (len(self.discard_cards[Suit.PURPLE]) > 0):
        #             self.discard_cards[Suit.PURPLE][len(self.discard_cards[Suit.PURPLE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 4)))
        #         else:
        #             self.discard_cards[Suit.PURPLE][0].cardprint(parameter, cord_y, (cord_x + (16 * 4)))

        #     if key == Suit.WHITE and self.discard_cards[Suit.WHITE]:
        #         if index == 6 and len(self.discard_cards[Suit.WHITE]) > 0:
        #             self.discard_cards[Suit.WHITE][len(self.discard_cards[Suit.WHITE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 5)))
        #         elif (len(self.discard_cards[Suit.WHITE]) > 0):
        #             self.discard_cards[Suit.WHITE][len(self.discard_cards[Suit.WHITE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 5)))
        #         else:
        #             self.discard_cards[Suit.WHITE][0].cardprint(parameter, cord_y, (cord_x + (16 * 5)))
