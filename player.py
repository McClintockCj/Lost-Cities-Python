
import curses
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

class player:

    def __init__(self, deck):
        self.hand_cards = []
        self.played_cards = []
        for i in range(1, 9):
            temp_card = deck.draw_card()
            temp_card.set_position(Position.HAND)
            self.hand_cards.append(temp_card)
        self.sort_hand()


    def sort_hand(self):
        self.hand_cards = sorted(self.hand_cards, key=lambda temp_card: (temp_card.suit.value, temp_card.num if temp_card.num != 'Wager' else 0))
        for card in self.hand_cards:
            card.set_hand_num(self.hand_cards.index(card) + 1)

    def sort_played(self):
        self.played_cards = sorted(self.played_cards, key=lambda temp_card: (temp_card.suit.value, temp_card.num if temp_card.num != 'Wager' else 0))

    def draw_to_hand(self, deck):
        temp_card = deck.draw_card()
        if temp_card != False:
            temp_card.set_position(Position.HAND)
            self.hand_cards.append(temp_card)
            self.sort_hand()
        else:
            return False

    def hand_cordinate(self, card, index):
        if card.hand_num == 1 and index == 1:
            return (28, 5)
        elif card.hand_num == 1:
            return (30, 5)
        if card.hand_num == 2 and index == 2:
            return (28, 21)
        elif card.hand_num == 2:
            return (30, 21)
        elif card.hand_num == 3 and index == 3:
            return (28, 37)
        elif card.hand_num == 3:
            return (30, 37)
        elif card.hand_num == 4 and index == 4:
            return (28, 53)
        elif card.hand_num == 4:
            return (30, 53)
        elif card.hand_num == 5 and index == 5:
            return (28, 69)
        elif card.hand_num == 5:
            return (30, 69)
        elif card.hand_num == 6 and index == 6:
            return (28, 85)
        elif card.hand_num == 6:
            return (30, 85)
        elif card.hand_num == 7 and index == 7:
            return (28, 101)
        elif card.hand_num == 7:
            return (30, 101)
        elif card.hand_num == 8 and index == 8:
            return (28, 117)
        elif card.hand_num == 8:   
            return (30, 117)
        
    def played_cordinate(self, card):
        if card.suit == Suit.RED:
            return (19, 5)
        elif card.suit == Suit.GREEN:
            return (19, 21)
        elif card.suit == Suit.BLUE:
            return (19, 37)
        elif card.suit == Suit.YELLOW:
            return (19, 53)
        elif card.suit == Suit.PURPLE:
            return (19, 69)
        # elif card.suit == Suit.WHITE:
        #     return (19, 85)
        
    def print_hand(self, parameter, index=1):
        for card in self.hand_cards:
            card.cardprint(parameter, self.hand_cordinate(card, index)[0], self.hand_cordinate(card, index)[1])

    def print_played(self, parameter):
        self.sort_played()
        Rcount = 0
        Gcount = 0
        Bcount = 0
        Ycount = 0
        Pcount = 0
        # Wcount = 0
        for card in self.played_cards:
            if card.suit == Suit.RED:
                card.cardprint(parameter, 10+(2*Rcount), 5)
                Rcount += 1
            elif card.suit == Suit.GREEN:
                card.cardprint(parameter, 10+(2*Gcount), 21)
                Gcount += 1
            elif card.suit == Suit.BLUE:
                card.cardprint(parameter, 10+(2*Bcount), 37)
                Bcount += 1
            elif card.suit == Suit.YELLOW:
                card.cardprint(parameter, 10+(2*Ycount), 53)
                Ycount += 1
            elif card.suit == Suit.PURPLE:
                card.cardprint(parameter, 10+(2*Pcount), 69)
                Pcount += 1

    
    def score(self):
        total_score = 0
        return total_score 
    
    def score(self):
        total_score = 0

        for suit in Suit:
            return total_score
        
    def turn(self, parameter, deck):
        index = 1
        while True:
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

            if (crc == curses.KEY_ENTER or crc == 10 or crc == 13 or crc == "\n"):
                if self.play(parameter, index, deck):
                    break
                # else:
                    # parameter.addstr(40, 5, "Invalid card.")
                
            self.print_hand(parameter, index)
            self.print_played(parameter)
            parameter.refresh()
        
    def play(self, parameter, index, deck):
        for card in self.hand_cards:
            if card.hand_num == index:
                self.hand_cards.remove(card)
                self.played_cards.append(card)
                self.print_played(parameter)
                if self.draw_to_hand(deck):
                    return True
                # else:
                #     parameter.addstr(40, 5, "The round is over!")
                #     parameter.refresh()
                #     return False


