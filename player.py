import curses
import time
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Suit

screen_rows = 48
screen_cols = 137

class player:
    """
    The player class represents a player in the Lost Cities game.

    Attributes:
        player_num (int): The player's number (1 or 2).
        hand_cards (list): The list of cards in the player's hand.
        played_cards (dict): A dictionary of played cards by suit.

    Methods:
        sort_hand(): Sorts the player's hand cards.
        sort_played(): Sorts the played cards by suit.
        hand_cordinate(card, index): Returns the (y, x) coordinates for a card in hand.
        print_hand(parameter, index=0): Prints the player's hand to the given curses window.
        print_played(parameter): Prints the player's played cards to the given curses window.
        score(): Calculates and returns the player's score.
    """
    def __init__(self, deck, player_num = 0):
        self.player_num = player_num
        self.hand_cards = []
        self.played_cards = {Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]}
        for _ in range(1, 9):
            temp_card = deck.draw_card()
            self.hand_cards.append(temp_card)
        self.sort_hand()


    def sort_hand(self):
        """
        This method sorts the player's hand cards.
        Parameters:
        None
        """
        self.hand_cards = sorted(self.hand_cards, key=lambda temp_card: (temp_card.suit.value, temp_card.num if temp_card.num != 'Wager' else 0))
        for card in self.hand_cards:
            card.hand_num = self.hand_cards.index(card) + 1

    def sort_played(self):
        """
        This method sorts the played cards by suit.
        Parameters:
        None
        """
        for suit in Suit:
            self.played_cards[suit] = sorted(self.played_cards[suit], key=lambda temp_card: (temp_card.num if temp_card.num != 'Wager' else 0))

    def hand_cordinate(self, card, index):
        """
        This method returns the (y, x) coordinates for a card in hand.
        Parameters:
        card (card): The card for which to get the coordinates.
        index (int): The index for positioning the card.
        Returns:
        tuple: The (y, x) coordinates for the card in hand.
        """
        x_start = 5
        y_start = screen_rows - 10

        if card.hand_num == index:
            return(y_start, x_start + (16 * (card.hand_num-1)))
        else:
            return (y_start + 2, x_start + (16 * (card.hand_num-1)))
        
    def print_hand(self, parameter, index=0):
        """
        This method prints the player's hand to the given curses window.
        Parameters:
        parameter: The curses window where the hand will be displayed.
        index (int): The index of the highlighted card.
        """
        for card in self.hand_cards:
            card.cardprint(parameter, self.hand_cordinate(card, index)[0], self.hand_cordinate(card, index)[1])

    def print_played(self, parameter):
        """
        This method prints the player's played cards to the given curses window.
        Parameters:
        parameter: The curses window where the played cards will be displayed.
        """
        y_start = screen_rows - 38
        x_start = 5
        self.sort_played()
        for key in self.played_cards.keys():
            for card in self.played_cards.get(key):
                if card.suit == Suit.RED:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.RED].index(card)), x_start)
                elif card.suit == Suit.GREEN:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.GREEN].index(card)), x_start + 16)
                elif card.suit == Suit.BLUE:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.BLUE].index(card)), x_start + (16 * 2))
                elif card.suit == Suit.YELLOW:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.YELLOW].index(card)), x_start + (16 * 3))
                elif card.suit == Suit.PURPLE:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.PURPLE].index(card)), x_start + (16 * 4))
                elif card.suit == Suit.WHITE:
                    card.cardprint(parameter, y_start + (2 * self.played_cards[Suit.WHITE].index(card)), x_start + (16 * 5))
        
    
    def score(self):
        """
        This method calculates and returns the player's total score.
        Returns:
        int: The total score of the player.
        """
        total_score = 0
        score_info = {}
        for suit in [Suit.RED, Suit.GREEN, Suit.BLUE, Suit.YELLOW, Suit.PURPLE, Suit.WHITE]:
            score_info[suit] = {"score": 0, "wage": 1, "neg": 0, "count": 0, "bonus": 0}
        
        for key in self.played_cards.keys():
            for card in self.played_cards.get(key):
                if card.suit == key:
                    score_info[key]["count"] += 1
                    score_info[key]["neg"] = 20
                    if card.num == 0:
                        score_info[key]["wage"] += 1
                    else:
                        score_info[key]["score"] += card.num

        for key in score_info.keys():
            if score_info[key]["count"] >= 8:
                score_info[key]["bonus"] = 20
            else:
                score_info[key]["bonus"] = 0

        for key in score_info.keys():
            total_score += ((score_info[key]["score"] - score_info[key]["neg"]) * score_info[key]["wage"]) + score_info[key]["bonus"]

        return total_score

        
    def turn(self, parameter, deck):
        """
        This method handles the player's turn.
        Parameters:
        parameter: The curses window where the game will be displayed.
        deck: The deck object representing the main deck and discard piles.
        """
        index = 1
        parameter.clear()
        deck.print_deck(parameter)
        self.print_played(parameter)
        self.print_hand(parameter, index)
        deck.print_discard(parameter)
        parameter.refresh()

        while True:
            comments = 0
            parameter.addstr(1, screen_cols- len("Mode: PLAY"), "Mode: PLAY", curses.color_pair(7))
            parameter.addstr(5, 120, "<-- DISCARD", curses.color_pair(7))
            parameter.addstr(14, 101, "<-- PLAYED CARDS", curses.color_pair(7))
            parameter.addstr(0, screen_cols - len(f"Player {self.player_num}"),  f"Player {self.player_num}", curses.color_pair(7))

            crc = parameter.getch()
            parameter.clear()

            if (crc == curses.KEY_RIGHT):
                if index == 8:
                    index = 1
                else:
                    index += 1
            
            if (crc == curses.KEY_LEFT):
                if index == 1:
                    index = 8
                else:
                    index -= 1

            if (crc == curses.KEY_UP):
                deck.discard(index, self.hand_cards)
                parameter.clear()
                deck.print_deck(parameter)
                self.print_played(parameter)
                self.print_hand(parameter, index)
                deck.print_discard(parameter)
                parameter.refresh()
                self.draw_to_hand(parameter, deck)
                break

            if (crc == curses.KEY_DOWN):
                if self.play(index):
                    parameter.clear()
                    deck.print_deck(parameter)
                    self.print_played(parameter)
                    self.print_hand(parameter, index)
                    deck.print_discard(parameter)
                    parameter.refresh()
                    self.draw_to_hand(parameter, deck)
                    break
                else:
                    comments = 1
                    parameter.refresh()

            parameter.clear()
            self.print_played(parameter)
            self.print_hand(parameter, index)
            if comments == 1:
                parameter.addstr(screen_rows - 1, 0, "The card must have a larger value then the previous played card of that suit.", curses.color_pair(7) | curses.A_BOLD)
            deck.print_deck(parameter)
            deck.print_discard(parameter)
            parameter.refresh()

        parameter.clear()
        deck.print_deck(parameter)
        self.print_hand(parameter, index)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()
        deck.last_card = 0

        
    def play(self, index):
        """
        This method plays a card from the player's hand to the played cards.
        Parameters:
        index (int): The index of the card to be played.
        Returns:
        bool: True if the card was successfully played, False otherwise.
        """
        for card in self.hand_cards:
            if card.hand_num == index:
                if (len(self.played_cards[Suit(card.suit)]) > 0):
                    if int(card.num) > int(self.played_cards.get(Suit(card.suit))[-1].num) or int(self.played_cards.get(Suit(card.suit))[-1].num) == 0:
                        self.hand_cards.remove(card)
                        self.played_cards[card.suit].append(card)
                        return True
                    else:
                        return False
                else:
                    self.hand_cards.remove(card)
                    self.played_cards[card.suit].append(card)
                    return True


    def draw_to_hand(self, parameter, deck):
        """
        This method allows the player to draw a card from the deck or discard pile.
        Parameters:
        parameter: The curses window where the game will be displayed.
        deck: The deck object representing the main deck and discard piles.
        """
        index = 7
        parameter.clear()
        deck.print_deck(parameter, index)
        self.print_hand(parameter)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()
        while True:
            parameter.addstr(1, screen_cols- len("Mode: DRAW"), "Mode: DRAW", curses.color_pair(7))
            parameter.addstr(5, 120, "<-- DISCARD", curses.color_pair(7))
            parameter.addstr(14, 101, "<-- PLAYED CARDS", curses.color_pair(7)) 
            parameter.addstr(0, screen_cols - len(f"Player {self.player_num}"),  f"Player {self.player_num}", curses.color_pair(7))
            crc = parameter.getch()

            if (crc == curses.KEY_RIGHT):
                if index == 7:
                    index = 1
                else:
                    index += 1
                while (index != 7 and len(deck.discard_cards[Suit(index)]) < 1):
                    index += 1
            
            if (crc == curses.KEY_LEFT):
                if index == 1:
                    index = 7
                else:
                    index -= 1
                    while (index != 7 and len(deck.discard_cards[Suit(index)]) < 1):
                        if index == 1:
                            index = 7
                            break
                        else:
                            index -= 1
                
            
            if (crc == curses.KEY_DOWN):
                if index == 7:
                    temp_card = deck.draw_card()
                    self.hand_cards.append(temp_card)
                    self.sort_hand()
                    break
                else:
                    temp_card = 0
                    if (len(deck.discard_cards[Suit(index)]) > 0):
                        temp_card = deck.discard_cards[Suit(index)][len(deck.discard_cards[Suit(index)]) - 1]
                        if (temp_card == deck.last_card):
                            parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                            continue
                        temp_card = deck.discard_cards[Suit(index)].pop()
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    else:
                        continue
                    break
                    

            parameter.clear()
            deck.print_deck(parameter, index)
            self.print_hand(parameter)
            self.print_played(parameter)
            deck.print_discard(parameter, index)
            parameter.refresh()

        
        parameter.clear()
        deck.print_deck(parameter)
        self.print_hand(parameter)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()

    
            

