import curses
import random
from curses import wrapper
import time
import rulebook
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Position, Suit
from deck import deck
from player import player, screen_rows, screen_cols



print (f'\x1b[8;{screen_rows};{screen_cols}t')
time.sleep(0.1)

def print(parameter, player, deck):
    parameter.clear()
    deck.print_deck(parameter)
    player.print_hand(parameter)
    deck.print_discard(parameter)
    player.print_played(parameter)
    parameter.refresh()

player1_string = [" _      _       _  _     _        _     _    ___      _     ", "|_| |  |_| |_| |_ |_|   | | |\ | |_  | |_     |  | | |_| |\ |", "|   |_ | |  _| |_ | \   |_| | \| |_     _|    |  |_| | \ | \|"]
player2_string = [" _      _       _  _   ___        _     _    ___      _     ", "|_| |  |_| |_| |_ |_|   |  |   | | | | |_     |  | | |_| |\ |", "|   |_ | |  _| |_ | \   |  |_|_| |_|    _|    |  |_| | \ | \|"]
end_of_game_string = [" _       _     _   _    _   _   _ _   _", "|_ |\ | | \   | | |_   |__ |_| | | | |_", "|_ | \| |_/   |_| |    |_| | | |   | |_"]


# Deck = deck()

# player1 = player(Deck)

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
    
    curses.init_pair(RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(BLUE_ON_BLACK, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(YELLOW_ON_BLACK, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(PURPLE_ON_BLACK, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(WHITE_ON_BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_WHITE)

    while True:
        intro = ["Welcome to Lost Cities!", "New Game", "Rule Book", "Exit", "Test"]
        loc_x = (screen_cols - 15)//2
        loc_y = 16

        idx = 1
        while True:
            stdscr.addstr(loc_y, loc_x, " ------------- ")
            stdscr.addstr(loc_y + 1, loc_x, "| Lost Cities |")
            stdscr.addstr(loc_y + 2, loc_x, "|             |")
            stdscr.addstr(loc_y + 3, loc_x, "|             |")
            stdscr.addstr(loc_y + 4, loc_x, "|             |")
            stdscr.addstr(loc_y + 5, loc_x, "|             |")
            stdscr.addstr(loc_y + 6, loc_x, "|             |")
            stdscr.addstr(loc_y + 7, loc_x, "| Lost Cities |")
            stdscr.addstr(loc_y + 8, loc_x, " ------------- ")

            for i, strings in enumerate(intro):
                if (i) == idx:
                    color_choice = BLUE_ON_BLACK
                else:
                    color_choice = GREEN_ON_BLACK

                stdscr.addstr(((screen_rows//2) + i),(screen_cols - len(strings))//2, strings, curses.color_pair(color_choice) | curses.A_BOLD)
            stdscr.refresh()
            
            choice = stdscr.getch()
            if (choice == curses.KEY_UP and idx > 1):
                idx -= 1
            elif (choice == curses.KEY_DOWN and idx <= (len(intro) - 2)):
                idx += 1

            if choice == curses.KEY_ENTER or choice == 10 or choice == 13 or choice == "\n":
                if idx == 1:
                    stdscr.clear()
                    Deck = deck()
                    Deck.new_deck()
                    player1 = player(Deck, 1)
                    player2 = player(Deck, 2)

                    while Deck.check_end():
                        for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player1_string[i]))//2, player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()

                        print(stdscr, player1, Deck)
                        player1.turn(stdscr, Deck)
                        stdscr.refresh()
                        # time.sleep(1)
                        stdscr.clear()

                        for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player2_string[i]))//2, player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()

                        print(stdscr, player2, Deck)
                        player2.turn(stdscr, Deck)
                        stdscr.refresh()
                        # time.sleep(1)
                        stdscr.clear()
                    else:
                        stdscr.clear()
                        score1 = f"Player 1 Score: {player1.score()}"
                        score2 = f"Player 2 Score: {player2.score()}"
                        stdscr.addstr(screen_rows//2 - 5, (screen_cols - len(score1))//2, score1, curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.addstr(screen_rows//2 + 5, (screen_cols - len(score2))//2, score2, curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()

                        stdscr.clear()
                        for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(end_of_game_string[i]))//2, end_of_game_string[i], curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()
                        stdscr.clear()

                elif idx == 2:
                    rulebook.rulebook(stdscr)
                    stdscr.clear()
                    stdscr.refresh()
                    return

                elif idx == 3:
                    stdscr.clear()
                    while True:
                        for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(end_of_game_string[i]))//2, end_of_game_string[i], curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.refresh()
                        time.sleep(3)
                        stdscr.clear()
                        exit()
                        break

                elif idx == 4:
                    test_suits = [Suit.RED, Suit.GREEN, Suit.BLUE]
                    stdscr.clear()
                    Deck = deck()
                    for suit in test_suits:
                        for _ in range(3):
                            temp_card1 = card(suit, 0, Position.DECK)
                            Deck.deck_cards.append(temp_card1)
                        for number in range(2, 11, 2):
                            temp_card2 = card(suit, number, Position.DECK)
                            Deck.deck_cards.append(temp_card2)
                    random.shuffle(Deck.deck_cards)
                    
                    player1 = player(Deck, 1)

                    while Deck.check_end():
                        print(stdscr, player1, Deck)
                        player1.turn(stdscr, Deck)
                        stdscr.refresh()
                        stdscr.clear()
                    else:
                        stdscr.clear()
                        score1 = f"Player 1 Score: {player1.score()}"
                        stdscr.addstr(screen_rows//2 - 5, (screen_cols - len(score1))//2, score1, curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()

                        stdscr.clear()
                        for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(end_of_game_string[i]))//2, end_of_game_string[i], curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
                        stdscr.refresh()
                        stdscr.getch()
                        stdscr.clear()



                

        stdscr.refresh()

        


        while Deck.check_end():
            Deck.print_deck(stdscr)
            player1.print_hand(stdscr)
            player1.print_played(stdscr)
            player1.turn(stdscr, Deck)
            stdscr.refresh()
        else:
            stdscr.clear()
            while True:
                stdscr.addstr(0, 0, "End of Game")
                stdscr.refresh()
                time.sleep(3)
                break


    

wrapper(main)

