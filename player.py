
import curses
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

class player:

    def __init__(self, deck):
        self.hand_cards = []
        self.played_cards = [] # I will impiment this tactic for played cards also: Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]
        self.discard_cards = {Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]}
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

    def hand_cordinate(self, card, index):

        if card.hand_num == index:
            return(40, 5 + (16 * (card.hand_num-1)))
        else:
            return (42, 5 + (16 * (card.hand_num-1)))
        
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
        Wcount = 0
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
            elif card.suit == Suit.WHITE:
                card.cardprint(parameter, 10+(2*Wcount), 85)
                Wcount += 1
    
    def score(self):
        R_score = 0
        R_wage = 1
        R_neg = 0

        G_score = 0
        G_wage = 1
        G_neg = 0

        B_score = 0
        B_wage = 1
        B_neg = 0

        Y_score = 0
        Y_wage = 1
        Y_neg = 0

        P_score = 0
        P_wage = 1
        P_neg = 0

        W_score = 0
        W_wage = 1
        W_neg = 0

        for card in self.played_cards:
            if card.suit == Suit.RED:
                R_neg = -20
                if card.num == 0:
                    R_wage += 1
                R_score += card.num
            if card.suit == Suit.GREEN:
                G_neg = -20
                if card.num == 0:
                    G_wage += 1
                G_score += card.num
            if card.suit == Suit.BLUE:
                B_neg = -20
                if card.num == 0:
                    B_wage += 1
                B_score += card.num
            if card.suit == Suit.YELLOW:
                Y_neg = -20
                if card.num == 0:
                    Y_wage += 1
                Y_score += card.num
            if card.suit == Suit.PURPLE:
                P_neg = -20
                if card.num == 0:
                    P_wage += 1
                P_score += card.num
            if card.suit == Suit.WHITE:
                W_neg = -20
                if card.num == 0:
                    W_wage += 1
                W_score += card.num

        total_score = ((R_neg - (R_score * R_wage))+(G_neg - (G_score * G_wage))+(B_neg - (B_score * B_wage))+(Y_neg - (Y_score * Y_wage))+(P_neg - (P_score * P_wage))+(W_neg - (W_score * W_wage)))
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

            if (crc == curses.KEY_UP):
                self.discard(index)
                parameter.addstr("TEST")
                self.draw_to_hand(parameter, deck)
                break
                # if self.play(parameter, index, deck):
                #     break
                # else:
                #     parameter.addstr(40, 5, "Invalid card.")
                # break

            if (crc == curses.KEY_DOWN):
                self.play(parameter, index)
                self.draw_to_hand(parameter, deck)
                break
                # if self.play(parameter, index, deck):
                #     break
                # else:
                #     parameter.addstr(40, 5, "Invalid card.")
                # break

            parameter.clear()
            deck.deck_print(parameter)
            self.print_hand(parameter, index)
            self.print_played(parameter)
            self.print_discard(parameter)
            parameter.refresh()
        
    def play(self, parameter, index):
        for card in self.hand_cards:
            if card.hand_num == index:
                self.hand_cards.remove(card)
                self.played_cards.append(card)
                self.print_played(parameter)
        


    def draw_to_hand(self, parameter, deck):
        index = 7
        while True:
            crc = parameter.getch()
            parameter.clear()

            if (crc == curses.KEY_RIGHT):
                if index == 7:
                    index = 1
                else:
                    index += 1
            
            if (crc == curses.KEY_LEFT):
                if index == 1:
                    index = 7
                else:
                    index -= 1

            if (crc == curses.KEY_DOWN):
                if index == 7:
                    temp_card = deck.draw_card()
                    temp_card.set_position(Position.HAND)
                    self.hand_cards.append(temp_card)
                    self.sort_hand()
                    break
                else:
                    if index == 1:
                        temp_card = self.discard_cards[Suit.RED].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    if index == 2:
                        temp_card = self.discard_cards[Suit.GREEN].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    if index == 3:
                        temp_card = self.discard_cards[Suit.BLUE].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    if index == 4:
                        temp_card = self.discard_cards[Suit.YELLOW].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    if index == 5:
                        temp_card = self.discard_cards[Suit.PURPLE].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    if index == 6:
                        temp_card = self.discard_cards[Suit.WHITE].pop(0)
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    break

            parameter.clear()
            deck.deck_print(parameter, index)
            self.print_hand(parameter)
            self.print_played(parameter)
            self.print_discard(parameter, index)
            parameter.refresh()

    def discard(self, index):
        for card in self.hand_cards:
            if card.hand_num == index:
                self.hand_cards.remove(card)
                card.set_position(Position.DISCARD)
                self.discard_cards[card.suit].append(card)

    def print_discard(self, parameter, index = 0):
        cord_x = 5
        cord_y = 1
        for key in self.discard_cards:
            if key == Suit.RED and self.discard_cards[Suit.RED]:
                if index == 1:
                    self.discard_cards[Suit.RED][0].cardprint(parameter, cord_y + 2, cord_x)
                else:
                    self.discard_cards[Suit.RED][0].cardprint(parameter, cord_y, cord_x)    

            if key == Suit.GREEN and self.discard_cards[Suit.GREEN]:
                if index == 2:
                    self.discard_cards[Suit.GREEN][0].cardprint(parameter, cord_y + 2, (cord_x + 16))
                else:
                    self.discard_cards[Suit.GREEN][0].cardprint(parameter, cord_y, (cord_x + 16))

            if key == Suit.BLUE and self.discard_cards[Suit.BLUE]:
                if index == 3:
                    self.discard_cards[Suit.BLUE][0].cardprint(parameter, cord_y + 2, (cord_x + (16 * 2)))
                else:
                    self.discard_cards[Suit.BLUE][0].cardprint(parameter, cord_y, (cord_x + (16 * 2)))

            if key == Suit.YELLOW and self.discard_cards[Suit.YELLOW]:
                if index == 4:
                    self.discard_cards[Suit.YELLOW][0].cardprint(parameter, cord_y + 2, (cord_x + (16 * 3)))
                else:
                    self.discard_cards[Suit.YELLOW][0].cardprint(parameter, cord_y, (cord_x + (16 * 3)))

            if key == Suit.PURPLE and self.discard_cards[Suit.PURPLE]:
                if index == 5:
                    self.discard_cards[Suit.PURPLE][0].cardprint(parameter, cord_y + 2, (cord_x + (16 * 4)))
                else:
                    self.discard_cards[Suit.PURPLE][0].cardprint(parameter, cord_y, (cord_x + (16 * 4)))

            if key == Suit.WHITE and self.discard_cards[Suit.WHITE]:
                if index == 6:
                    self.discard_cards[Suit.WHITE][0].cardprint(parameter, cord_y + 2, (cord_x + (16 * 5)))
                else:
                    self.discard_cards[Suit.WHITE][0].cardprint(parameter, cord_y, (cord_x + (16 * 5)))
            

