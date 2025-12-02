import curses
import time
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

# Moved here to avoid circular import
screen_rows = 52
screen_cols = 137

class player:

    def __init__(self, deck, player_num = 0):
        self.player_num = player_num
        self.hand_cards = []
        self.played_cards = {Suit.RED :[], Suit.GREEN:[], Suit.BLUE:[], Suit.YELLOW:[], Suit.PURPLE:[], Suit.WHITE:[]}
        for _ in range(1, 9):
            temp_card = deck.draw_card()
            temp_card.set_position(Position.HAND)
            self.hand_cards.append(temp_card)
        self.sort_hand()


    def sort_hand(self):
        self.hand_cards = sorted(self.hand_cards, key=lambda temp_card: (temp_card.suit.value, temp_card.num if temp_card.num != 'Wager' else 0))
        for card in self.hand_cards:
            card.set_hand_num(self.hand_cards.index(card) + 1)

    def sort_played(self):
        for suit in Suit:
            self.played_cards[suit] = sorted(self.played_cards[suit], key=lambda temp_card: (temp_card.num if temp_card.num != 'Wager' else 0))

    def hand_cordinate(self, card, index):

        if card.hand_num == index:
            return(40, 5 + (16 * (card.hand_num-1)))
        else:
            return (42, 5 + (16 * (card.hand_num-1)))
        
    def print_hand(self, parameter, index=0):
        for card in self.hand_cards:
            card.cardprint(parameter, self.hand_cordinate(card, index)[0], self.hand_cordinate(card, index)[1])

    def print_played(self, parameter):
        x_start = 11
        self.sort_played()
        for key in self.played_cards.keys():
            for card in self.played_cards.get(key):
                if card.suit == Suit.RED:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.RED].index(card)), 5)
                elif card.suit == Suit.GREEN:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.GREEN].index(card)), 21)
                elif card.suit == Suit.BLUE:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.BLUE].index(card)), 37)
                elif card.suit == Suit.YELLOW:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.YELLOW].index(card)), 53)
                elif card.suit == Suit.PURPLE:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.PURPLE].index(card)), 69)
                elif card.suit == Suit.WHITE:
                    card.cardprint(parameter, x_start + (2 * self.played_cards[Suit.WHITE].index(card)), 85)
        
    
    def score(self):
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

    # def score(self):
    #     R_score = 0
    #     R_wage = 1
    #     R_neg = 0
    #     R_count = 0

    #     G_score = 0
    #     G_wage = 1
    #     G_neg = 0
    #     G_count = 0

    #     B_score = 0
    #     B_wage = 1
    #     B_neg = 0
    #     B_count = 0

    #     Y_score = 0
    #     Y_wage = 1
    #     Y_neg = 0
    #     Y_count = 0

    #     P_score = 0
    #     P_wage = 1
    #     P_neg = 0
    #     P_count = 0

    #     W_score = 0
    #     W_wage = 1
    #     W_neg = 0
    #     W_count = 0

    #     for key in self.played_cards.keys():
    #         for card in self.played_cards.get(key):
    #                 if card.suit == Suit.RED:
    #                     R_count += 1
    #                     R_neg = 20
    #                     if card.num == 0:
    #                         R_wage += 1
    #                     R_score += card.num
    #                 if card.suit == Suit.GREEN:
    #                     G_count += 1
    #                     G_neg = 20
    #                     if card.num == 0:
    #                         G_wage += 1
    #                     G_score += card.num
    #                 if card.suit == Suit.BLUE:
    #                     B_count += 1
    #                     B_neg = 20
    #                     if card.num == 0:
    #                         B_wage += 1
    #                     B_score += card.num
    #                 if card.suit == Suit.YELLOW:
    #                     Y_count += 1
    #                     Y_neg = 20
    #                     if card.num == 0:
    #                         Y_wage += 1
    #                     Y_score += card.num
    #                 if card.suit == Suit.PURPLE:
    #                     P_count += 1
    #                     P_neg = 20
    #                     if card.num == 0:
    #                         P_wage += 1
    #                     P_score += card.num
    #                 if card.suit == Suit.WHITE:
    #                     W_count += 1
    #                     W_neg = 20
    #                     if card.num == 0:
    #                         W_wage += 1
    #                     W_score += card.num

    #     total_score = (((R_score - R_neg) * R_wage) + R_count) + (((G_score - G_neg) * G_wage) + G_count) + (((B_score - B_neg) * B_wage) + B_count) + (((Y_score - Y_neg) * Y_wage) + Y_count) + (((P_score - P_neg) * P_wage) + P_count) + (((W_score - W_neg) * W_wage) + W_count)
    #     return total_score

        
    def turn(self, parameter, deck):
        index = 1
        parameter.clear()
        deck.print_deck(parameter)
        self.print_hand(parameter, index)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()

        while True:
            comments = 0
            parameter.addstr(0, 0, "Mode: PLAY", curses.color_pair(7))
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
                self.print_hand(parameter, index)
                self.print_played(parameter)
                deck.print_discard(parameter)
                parameter.refresh()
                self.draw_to_hand(parameter, deck)
                break

            if (crc == curses.KEY_DOWN):
                if self.play(index):
                    parameter.clear()
                    deck.print_deck(parameter)
                    self.print_hand(parameter, index)
                    self.print_played(parameter)
                    deck.print_discard(parameter)
                    parameter.refresh()
                    self.draw_to_hand(parameter, deck)
                    break
                else:
                    comments = 1
                    parameter.refresh()

            parameter.clear()
            if comments == 1:
                parameter.addstr(screen_rows - 1, 0, "The card must have a larger value then the previous played card of that suit.", curses.color_pair(7) | curses.A_BOLD)
            deck.print_deck(parameter)
            self.print_hand(parameter, index)
            self.print_played(parameter)
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
        indx = 7
        parameter.clear()
        deck.print_deck(parameter, indx)
        self.print_hand(parameter)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()
        while True:
            parameter.addstr(0, 0, "Mode: DRAW", curses.color_pair(7))
            parameter.addstr(5, 120, "<-- DISCARD", curses.color_pair(7))
            parameter.addstr(14, 101, "<-- PLAYED CARDS", curses.color_pair(7)) 
            parameter.addstr(0, screen_cols - len(f"Player {self.player_num}"),  f"Player {self.player_num}", curses.color_pair(7))
            crc = parameter.getch()

            if (crc == curses.KEY_RIGHT):
                if indx == 7:
                    indx = 1
                else:
                    indx += 1
                while (indx != 7 and len(deck.discard_cards[Suit(indx)]) < 1):
                    indx += 1
            
            if (crc == curses.KEY_LEFT):
                if indx == 1:
                    indx = 7
                else:
                    indx -= 1
                    while (indx != 7 and len(deck.discard_cards[Suit(indx)]) < 1):
                        if indx == 1:
                            indx = 7
                            break
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
                    # I love shortening code like this
                    temp_card = 0
                    if (len(deck.discard_cards[Suit(indx)]) > 0):
                        temp_card = deck.discard_cards[Suit(indx)][len(deck.discard_cards[Suit(indx)]) - 1]
                        if (temp_card == deck.last_card):
                            parameter.addstr(11, 60, "Invalid", curses.color_pair(7))
                            continue
                        temp_card = deck.discard_cards[Suit(indx)].pop()
                        temp_card.set_position(Position.HAND)
                        self.hand_cards.append(temp_card)
                        self.sort_hand()
                    else:
                        continue
                    break
                    

            parameter.clear()
            deck.print_deck(parameter, indx)
            self.print_hand(parameter)
            self.print_played(parameter)
            deck.print_discard(parameter, indx)
            parameter.refresh()

        # Added so that if we break out of the loop, it still reprints right away
        parameter.clear()
        deck.print_deck(parameter)
        self.print_hand(parameter)
        self.print_played(parameter)
        deck.print_discard(parameter)
        parameter.refresh()

    
            

