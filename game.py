import curses
from player import player, screen_rows, screen_cols
from deck import deck
from card import RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK


class Game_Type:
    Pass_and_Play = 1
    Host = 2
    Join = 3

class Game:
    def __init__(self, parameter, type = Game_Type.Pass_and_Play):
        self.parameter = parameter
        self.game_type = type
        self.player1_string = [" _      _       _  _     _        _     _    ___      _     ", "|_| |  |_| |_| |_ |_|   | | |\\ | |_  | |_     |  | | |_| |\\ |", "|   |_ | |  _| |_ | \\   |_| | \\| |_     _|    |  |_| | \\ | \\|"]
        self.player2_string = [" _      _       _  _   ___        _     _    ___      _     ", "|_| |  |_| |_| |_ |_|   |  |   | | | | |_     |  | | |_| |\\ |", "|   |_ | |  _| |_ | \\   |  |_|_| |_|    _|    |  |_| | \\ | \\|"]
        self.end_of_game_string = [" _       _     _   _    _   _   _ _   _", "|_ |\\ | | \\   | | |_   |__ |_| | | | |_", "|_ | \\| |_/   |_| |    |_| | | |   | |_"]
        

    def start_game(self):
        if self.game_type == Game_Type.Pass_and_Play:
            self.Pass_and_Play()
        elif self.game_type == Game_Type.Host:
            self.Host()
        elif self.game_type == Game_Type.Join:
            self.Join()

    def Pass_and_Play(self):
        self.parameter.clear()
        Deck = deck()
        Deck.new_deck()
        player1 = player(Deck, 1)
        player2 = player(Deck, 2)

        while Deck.check_end():
            for i in range(3):
                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player1_string[i]))//2, self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
            self.parameter.refresh()
            self.parameter.getch()

            print(self.parameter, player1, Deck)
            player1.turn(self.parameter, Deck)
            self.parameter.refresh()
            self.parameter.clear()

            for i in range(3):
                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player2_string[i]))//2, self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
            self.parameter.refresh()
            self.parameter.getch()

            print(self.parameter, player2, Deck)
            player2.turn(self.parameter, Deck)
            self.parameter.refresh()
            self.parameter.clear()
        else:
            self.parameter.clear()
            score1 = f"Player 1 Score: {player1.score()}"
            score2 = f"Player 2 Score: {player2.score()}"
            self.parameter.addstr(screen_rows//2 - 5, (screen_cols - len(score1))//2, score1, curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
            self.parameter.addstr(screen_rows//2 + 5, (screen_cols - len(score2))//2, score2, curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
            self.parameter.refresh()
            self.parameter.getch()

            self.parameter.clear()
            for i in range(3):
                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.end_of_game_string[i]))//2, self.end_of_game_string[i], curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
            self.parameter.refresh()
            self.parameter.getch()
            self.parameter.clear()

    def Host(self):
        pass

    def Join(self):
        pass
