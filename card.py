import curses
from enum import Enum, auto

RED_ON_BLACK = 1
GREEN_ON_BLACK = 2
BLUE_ON_BLACK = 3
YELLOW_ON_BLACK = 4
PURPLE_ON_BLACK = 5
WHITE_ON_BLACK = 6

class Position(Enum):
    DECK = auto()
    DISCARD = auto()
    HAND = auto()
    PLAYED = auto()

class Suit(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    PURPLE = 5
    WHITE = 6


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

        for suit in Suit:
            if self.suit == suit:
                color_choice = curses.color_pair(suit.value)

        parameter.attron(color_choice)

        if self.num == 0:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, "|    WAGER    |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            #parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "|    WAGER    |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")

        elif self.num < 10:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}           |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            #parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, f"|           {self.num} |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")
        else:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}          |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            #parameter.addstr(loc_y + 6, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, f"|          {self.num} |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")

        parameter.attroff(color_choice)

    

        
