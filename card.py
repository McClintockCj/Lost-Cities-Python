import curses
from enum import Enum, auto

# Color Pairs
RED_ON_BLACK = 1
GREEN_ON_BLACK = 2
BLUE_ON_BLACK = 3
YELLOW_ON_BLACK = 4
PURPLE_ON_BLACK = 5
WHITE_ON_BLACK = 6

class Suit(Enum):
    """
    Enumeration for the different suits/colors in the Lost Cities game.
    Attributes:
        RED (int): Represents the RED suit.
        GREEN (int): Represents the GREEN suit.
        BLUE (int): Represents the BLUE suit.
        YELLOW (int): Represents the YELLOW suit.
        PURPLE (int): Represents the PURPLE suit.
        WHITE (int): Represents the WHITE suit.
    """
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    PURPLE = 5
    WHITE = 6


class card:
    """
    the card class represents a single card in the Lost Cities game.

    Attributes:
        suit (Suit): The color/suit of the card (RED, GREEN, BLUE, YELLOW, PURPLE, WHITE).
        num (int): The number on the card (0 for Wager cards, 2-10 for number cards).
        hand_num (int): The index of the card in a player's hand (if applicable).
    """
    def __init__(self, suit, num, hand_num = 0):
        self.suit = suit
        self.num = num
        self.hand_num = hand_num

    def cardprint(self, parameter, y, x):
        """
        This method prints the card to the given curses window at the specified (y, x) location.
        Parameters:
        parameter: The curses window where the card will be printed.
        y (int): The y-coordinate for the card's position.
        x (int): The x-coordinate for the card's position.

        """

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
            parameter.addstr(loc_y + 6, loc_x, "|    WAGER    |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")

        elif self.num < 10:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}           |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, f"|           {self.num} |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")
        else:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, f"| {self.num}          |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, f"|          {self.num} |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")

        parameter.attroff(color_choice)

    

        
