
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit

class hand:

    def __init__(self, deck):
        self.hand_cards = []
        for i in range(1, 9):
            temp_card = deck.draw_card()
            temp_card.set_position(Position.HAND)
            self.hand_cards.append(temp_card)
        self.sort()


    def sort(self):
        self.hand_cards = sorted(self.hand_cards, key=lambda temp_card: (temp_card.suit.value, temp_card.num if temp_card.num != 'Wager' else 0))
        for card in self.hand_cards:
            card.set_hand_num(self.hand_cards.index(card) + 1)

    def hand_cordinate(self, card):
        if card.hand_num == 1:
            return (30, 5)
        elif card.hand_num == 2:
            return (30, 21)
        elif card.hand_num == 3:
            return (30, 37)
        elif card.hand_num == 4:
            return (30, 53)
        elif card.hand_num == 5:
            return (30, 69)
        elif card.hand_num == 6:
            return (30, 85)
        elif card.hand_num == 7:
            return (30, 101)
        elif card.hand_num == 8:   
            return (30, 117)
        
    def print_hand(self, parameter):
        for card in self.hand_cards:
            card.cardprint(parameter, self.hand_cordinate(card)[0], self.hand_cordinate(card)[1])

