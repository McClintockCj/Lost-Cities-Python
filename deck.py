import curses
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Suit
import random
from player import screen_rows, screen_cols

class deck():
    """
    The deck class represents a deck of cards in the Lost Cities game.

    Attributes:
        deck_cards (list): The list of cards currently in the deck.
        last_card (card): The last card drawn from the deck.
        full_deck (list): A copy of the full deck of cards.
        discard_cards (dict): A dictionary of discarded cards by suit.

    Methods:
        draw_card(): Draws a card from the deck.
        new_deck(): Initializes a new shuffled deck of cards.
        check_end(): Checks if the deck is empty.
        print_deck(parameter, index=0): Prints the deck to the given curses window.
        discard(index, players_cards=None): Discards a card from the player's hand to the discard pile.
        print_discard(parameter, index=0): Prints the discard piles to the given curses window
    """
    def __init__(self, deck_cards = []):
        self.deck_cards = deck_cards
        self.last_card = 0
        self.full_deck = deck_cards.copy()
        self.discard_cards = {Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]}

    def draw_card(self):
        """
        This method draws a card from the deck.
        Returns:
            card: The drawn card, or False if the deck is empty.
        """
        if self.deck_cards:
            return self.deck_cards.pop()
        else:
            return False

    def new_deck(self):
        """
        This method initializes a new shuffled deck of cards.
        6 Suits: RED, GREEN, BLUE, YELLOW, PURPLE, WHITE
        Each suit has:
            - 3 Wager cards (represented by number 0)
            - Numbered cards from 2 to 10
        """
        self.deck_cards.clear()
        self.full_deck.clear()
        for suit in Suit:
            for _ in range(3):
                temp_card1 = card(suit, 0)
                self.deck_cards.append(temp_card1)
            for number in range(2, 11):
                temp_card2 = card(suit, number)
                self.deck_cards.append(temp_card2)

        random.shuffle(self.deck_cards)
        self.full_deck = self.deck_cards.copy()

    def check_end(self):
        """
        This method checks if the deck is empty.
        Returns:
            bool: True if the deck has cards, False if empty.
        """
        if not self.deck_cards:
            return False
        else:
            return True
    
    def print_deck(self, parameter, index = 0):
        """
        This method prints the deck to the given curses window.
        Parameters:
            parameter: The curses window where the deck will be printed.
            index (int): The index for positioning the deck display.
        """
        loc_x = 101
        
        if index == 7:
            loc_y = 2
            parameter.addstr(1, loc_x, f"       {len(self.deck_cards)}/{len(self.full_deck)}")
        else:
            loc_y = 1

        if len(self.deck_cards) >= 3:
            parameter.addstr(loc_y, loc_x, " --------------- ")
            parameter.addstr(loc_y + 1, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|||             |")
            parameter.addstr(loc_y + 3, loc_x, "|||             |")
            parameter.addstr(loc_y + 4, loc_x, "|||             |")
            parameter.addstr(loc_y + 5, loc_x, "|||             |")
            parameter.addstr(loc_y + 6, loc_x, "||| Lost Cities |")
            parameter.addstr(loc_y + 7, loc_x, " --------------- ")
        elif len(self.deck_cards) == 2:
            parameter.addstr(loc_y, loc_x, " -------------- ")
            parameter.addstr(loc_y + 1, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "||             |")
            parameter.addstr(loc_y + 3, loc_x, "||             |")
            parameter.addstr(loc_y + 4, loc_x, "||             |")
            parameter.addstr(loc_y + 5, loc_x, "||             |")
            parameter.addstr(loc_y + 6, loc_x, "|| Lost Cities |")
            parameter.addstr(loc_y + 7, loc_x, " -------------- ")
        elif len(self.deck_cards) >= 1:
            parameter.addstr(loc_y, loc_x, " ------------- ")
            parameter.addstr(loc_y + 1, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 2, loc_x, "|             |")
            parameter.addstr(loc_y + 3, loc_x, "|             |")
            parameter.addstr(loc_y + 4, loc_x, "|             |")
            parameter.addstr(loc_y + 5, loc_x, "|             |")
            parameter.addstr(loc_y + 6, loc_x, "| Lost Cities |")
            parameter.addstr(loc_y + 7, loc_x, " ------------- ")
        

    def discard(self, index, players_cards = None):
        """
        This method discards a card from the player's hand to the discard pile.
        Parameters:
            index (int): The index of the card to discard.
            players_cards (list): The list of cards in the player's hand.
        """
        for card in players_cards:
            if card.hand_num == index:
                self.last_card = card
                players_cards.remove(card)
                self.discard_cards[card.suit].append(card)

    def print_discard(self, parameter, index = 0):
        """
        This method prints the discard piles to the given curses window.
        Parameters:
            parameter: The curses window where the discard pile will be printed.
            index (int): The index for highlighting a specific discard pile.
        """
        cord_x = 5
        cord_y = 1
        y_select_jump = 1

        color_choice = curses.A_NORMAL
        
        for key in self.discard_cards.keys():
            color_choice = curses.color_pair(key.value)
            if (len(self.discard_cards[key]) > 0):
                if key.value == index:
                    adjust_y = 0
                    self.discard_cards[key][-1].cardprint(parameter, cord_y + y_select_jump, cord_x + (16 * (key.value -1)))

                    if len(self.discard_cards[key]) > 1:
                        for i, card in enumerate(self.discard_cards[key][:-1]):
                            if len(self.discard_cards[key]) >= 9 and i == (len(self.discard_cards[key]) - 9):
                                parameter.addstr(cord_y, cord_x + (16 * (key.value -1)) + adjust_y, "+|", color_choice)
                                adjust_y += 2
                                continue
                            elif len(self.discard_cards[key]) >= 9 and i < (len(self.discard_cards[key]) - 7):
                                continue
                            else:
                                if card.num == 0:
                                    parameter.addstr(cord_y, cord_x + (16 * (key.value -1)) + adjust_y, "W|", color_choice)
                                    adjust_y += 2
                                elif card.num == 10:
                                    parameter.addstr(cord_y, cord_x + (16 * (key.value -1)) + adjust_y, f"{card.num}|", color_choice)
                                    adjust_y += 3
                                else:
                                    parameter.addstr(cord_y, cord_x + (16 * (key.value -1)) + adjust_y, f"{card.num}|", color_choice)
                                    adjust_y += 2
                else:
                    self.discard_cards[key][-1].cardprint(parameter, cord_y, cord_x + (16 * (key.value -1)))
            
