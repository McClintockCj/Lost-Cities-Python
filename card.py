import curses
from enum import Enum, auto

RED_ON_BLACK = 1
GREEN_ON_BLACK = 2
BLUE_ON_BLACK = 3
YELLOW_ON_BLACK = 4
PURPLE_ON_BLACK = 5
WHITE_ON_BLACK = 6

Red_card = 0
Green_card = 0
Blue_card = 0
Yellow_card = 0
Purple_card = 0
White_card = 0

class Position(Enum):
    DECK = auto()
    DISCARD = auto()
    HAND = auto()
    PLAYED = auto()

class Suit(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    PURPLE = auto()


class card:

    def __init__(self, suit, num, position = Position.DECK, hand_num = 0):
        self.suit = suit
        self.num = num
        self.position = position
        self.hand_num = hand_num

    def set_position(self, position):
        self.position = position

    def set_hand_num(self, hand_num):
        self.hand_num = hand_num

    def get_hand_num(self):
        return self.hand_num

    def cardprint(self, parameter, y, x):
        loc_x = x
        loc_y = y 

        color_choice = curses.A_NORMAL

        if self.suit == Suit.RED:
            color_choice = curses.color_pair(RED_ON_BLACK)
            if self.position == Position.DISCARD:
                loc_y = 5
                loc_x = 5
        elif self.suit == Suit.GREEN:
            color_choice = curses.color_pair(GREEN_ON_BLACK)
            if self.position == Position.DISCARD:
                loc_y = 5
                loc_x = 21
        elif self.suit == Suit.BLUE:
            color_choice = curses.color_pair(BLUE_ON_BLACK)
            if self.position == Position.DISCARD:
                loc_y = 5
                loc_x = 37
        elif self.suit == Suit.YELLOW:
            color_choice = curses.color_pair(YELLOW_ON_BLACK)
            if self.position == Position.DISCARD:
                loc_y = 5
                loc_x = 53
        elif self.suit == Suit.PURPLE:
            color_choice = curses.color_pair(PURPLE_ON_BLACK)
            if self.position == Position.DISCARD:
                loc_y = 5
                loc_x = 69

        parameter.attron(color_choice)

        if self.num == 'Wager':
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, "|    WAGER    |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 7, loc_x, "|    WAGER    |")
            parameter.addstr(loc_y + 8, loc_x, " ------------- ")

        elif self.num < 10:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}           |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 7, loc_x, f"|           {self.num} |")
            parameter.addstr(loc_y + 8, loc_x, " ------------- ")
        else:
            parameter.addstr(loc_y, loc_x, " ------------ ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}          |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 7, loc_x, f"|          {self.num} |")
            parameter.addstr(loc_y + 8, loc_x, " ------------- ")

        parameter.attroff(color_choice)
