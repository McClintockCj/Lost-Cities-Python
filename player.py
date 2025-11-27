
import curses
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

class player:

    def __init__(self, deck):
        self.hand_cards = []
        self.last_card = []
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
            parameter.addstr(0, 0, "Mode: PLAY", curses.color_pair(7))
            parameter.addstr(5, 120, "<-- DISCARD", curses.color_pair(7))
            parameter.addstr(14, 101, "<-- PLAYED CARDS", curses.color_pair(7))

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
                #Here to avoid unneccesary black screen
                parameter.clear()
                deck.deck_print(parameter)
                self.print_hand(parameter, index)
                self.print_played(parameter)
                self.print_discard(parameter)
                parameter.refresh()

                self.draw_to_hand(parameter, deck)
                break
                # if self.play(parameter, index, deck):
                #     break
                # else:
                #     parameter.addstr(40, 5, "Invalid card.")
                # break

            if (crc == curses.KEY_DOWN):
                self.play(parameter, index)

                #Here to avoid unneccesary black screen
                parameter.clear()
                deck.deck_print(parameter)
                self.print_hand(parameter, index)
                self.print_played(parameter)
                self.print_discard(parameter)
                parameter.refresh()

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
        


    def draw_to_hand(self, parameter, deck):
        indx = 7 #Was inside the loop resetting index back to 7 every time, made me pull my hair out :((((( -Charlie
        while True:
            parameter.addstr(0, 0, "Mode: DRAW", curses.color_pair(7))
            parameter.addstr(5, 120, "<-- DISCARD", curses.color_pair(7))
            parameter.addstr(14, 101, "<-- PLAYED CARDS", curses.color_pair(7))
            crc = parameter.getch()

            if (crc == curses.KEY_RIGHT):
                if indx == 7:
                    indx = 1
                else:
                    indx += 1
            
            if (crc == curses.KEY_LEFT):
                if indx == 1:
                    indx = 7
                else:
                    indx -= 1
            
            if (crc == curses.KEY_DOWN):
                if indx == 7:
                    temp_card = deck.draw_card()
                    temp_card.set_position(Position.HAND)
                    self.hand_cards.append(temp_card)
                    self.sort_hand()
                    break
                else:
                    if indx == 1:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.RED]) > 0):
                            temp_card = self.discard_cards[Suit.RED][len(self.discard_cards[Suit.RED]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.RED].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break

                    if indx == 2:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.GREEN]) > 0):
                            temp_card = self.discard_cards[Suit.GREEN][len(self.discard_cards[Suit.GREEN]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.GREEN].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break
                    if indx == 3:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.BLUE]) > 0):
                            temp_card = self.discard_cards[Suit.BLUE][len(self.discard_cards[Suit.BLUE]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.BLUE].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break
                    if indx == 4:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.YELLOW]) > 0):
                            temp_card = self.discard_cards[Suit.YELLOW][len(self.discard_cards[Suit.YELLOW]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.YELLOW].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break
                    if indx == 5:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.PURPLE]) > 0):
                            temp_card = self.discard_cards[Suit.PURPLE][len(self.discard_cards[Suit.PURPLE]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.PURPLE].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break
                    if indx == 6:
                        temp_card = 0
                        if (len(self.discard_cards[Suit.WHITE]) > 0):
                            temp_card = self.discard_cards[Suit.WHITE][len(self.discard_cards[Suit.WHITE]) - 1]
                            if (temp_card == self.last_card):
                                parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                                continue
                            temp_card = self.discard_cards[Suit.WHITE].pop()
                            temp_card.set_position(Position.HAND)
                            self.hand_cards.append(temp_card)
                            self.sort_hand()
                        else:
                            continue
                        break
                    

            parameter.clear()
            deck.deck_print(parameter, indx)
            self.print_hand(parameter)
            self.print_played(parameter)
            self.print_discard(parameter, indx)
            parameter.refresh()

    def discard(self, index):
        for card in self.hand_cards:
            if card.hand_num == index:
                self.last_card = card
                self.hand_cards.remove(card)
                card.set_position(Position.DISCARD)
                self.discard_cards[card.suit].append(card)

    def print_discard(self, parameter, index = 0):
        cord_x = 5
        cord_y = 1
        for key in self.discard_cards:
            if key == Suit.RED and self.discard_cards[Suit.RED]:
                if index == 1 and len(self.discard_cards[Suit.RED]) > 0:
                    self.discard_cards[Suit.RED][len(self.discard_cards[Suit.RED]) - 1].cardprint(parameter, cord_y + 2, cord_x)
                elif (len(self.discard_cards[Suit.RED]) > 0):
                    self.discard_cards[Suit.RED][len(self.discard_cards[Suit.RED]) - 1].cardprint(parameter, cord_y, cord_x)   
                else:
                    self.discard_cards[Suit.RED][0].cardprint(parameter, cord_y, cord_x)

            if key == Suit.GREEN and self.discard_cards[Suit.GREEN]:
                if index == 2 and len(self.discard_cards[Suit.GREEN]) > 0:
                    self.discard_cards[Suit.GREEN][len(self.discard_cards[Suit.GREEN]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16)))
                elif (len(self.discard_cards[Suit.GREEN]) > 0):
                    self.discard_cards[Suit.GREEN][len(self.discard_cards[Suit.GREEN]) - 1].cardprint(parameter, cord_y, (cord_x + (16)))   
                else:
                    self.discard_cards[Suit.GREEN][0].cardprint(parameter, cord_y, cord_x)

            if key == Suit.BLUE and self.discard_cards[Suit.BLUE]:
                if index == 3 and len(self.discard_cards[Suit.BLUE]) > 0:
                    self.discard_cards[Suit.BLUE][len(self.discard_cards[Suit.BLUE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 2)))
                elif (len(self.discard_cards[Suit.BLUE]) > 0):
                    self.discard_cards[Suit.BLUE][len(self.discard_cards[Suit.BLUE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 2)))
                else:
                    self.discard_cards[Suit.BLUE][0].cardprint(parameter, cord_y, (cord_x + (16 * 2)))

            if key == Suit.YELLOW and self.discard_cards[Suit.YELLOW]:
                if index == 4 and len(self.discard_cards[Suit.YELLOW]) > 0:
                    self.discard_cards[Suit.YELLOW][len(self.discard_cards[Suit.YELLOW]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 3)))
                elif (len(self.discard_cards[Suit.YELLOW]) > 0):
                    self.discard_cards[Suit.YELLOW][len(self.discard_cards[Suit.YELLOW]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 3)))
                else:
                    self.discard_cards[Suit.YELLOW][0].cardprint(parameter, cord_y, (cord_x + (16 * 3)))

            if key == Suit.PURPLE and self.discard_cards[Suit.PURPLE]:
                if index == 5 and len(self.discard_cards[Suit.PURPLE]) > 0:
                    self.discard_cards[Suit.PURPLE][len(self.discard_cards[Suit.PURPLE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 4)))
                elif (len(self.discard_cards[Suit.PURPLE]) > 0):
                    self.discard_cards[Suit.PURPLE][len(self.discard_cards[Suit.PURPLE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 4)))
                else:
                    self.discard_cards[Suit.PURPLE][0].cardprint(parameter, cord_y, (cord_x + (16 * 4)))

            if key == Suit.WHITE and self.discard_cards[Suit.WHITE]:
                if index == 6 and len(self.discard_cards[Suit.WHITE]) > 0:
                    self.discard_cards[Suit.WHITE][len(self.discard_cards[Suit.WHITE]) - 1].cardprint(parameter, cord_y + 2, (cord_x + (16 * 5)))
                elif (len(self.discard_cards[Suit.WHITE]) > 0):
                    self.discard_cards[Suit.WHITE][len(self.discard_cards[Suit.WHITE]) - 1].cardprint(parameter, cord_y, (cord_x + (16 * 5)))
                else:
                    self.discard_cards[Suit.WHITE][0].cardprint(parameter, cord_y, (cord_x + (16 * 5)))
            

