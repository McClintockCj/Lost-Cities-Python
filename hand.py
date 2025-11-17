
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

class hand:

    def __init__(self, hand_cards = []):
        self.hand_cards = hand_cards

    def new_hand(self, deck):
        for i in range(1, 9):
            temp_card = deck.draw_card()
            temp_card.set_position(Position.HAND)
            temp_card.set_hand_num(i)
            self.hand_cards.append(temp_card)
        return deck

    def hand_cordinate(self, card):
        if card.hand_num == 1:
            return (20, 5)
        elif card.hand_num == 2:
            return (20, 21)
        elif card.hand_num == 3:
            return (20, 37)
        elif card.hand_num == 4:
            return (20, 53)
        elif card.hand_num == 5:
            return (20, 69)
        elif card.hand_num == 6:
            return (20, 85)
        elif card.hand_num == 7:
            return (20, 101)
        elif card.hand_num == 8:   
            return (20, 117)
        
    def print_hand(self, parameter):
        for card in self.hand_cards:
            card.cardprint(parameter, self.hand_cordinate(card)[0], self.hand_cordinate(card)[1])

