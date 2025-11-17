import curses
from curses import wrapper
import time
from card import card, RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK, Red_card, Green_card, Blue_card, Yellow_card, Purple_card, White_card, Position, Suit
from deck import deck
from hand import hand
from play import play

screen_rows = 40
screen_cols = 137

print (f'\x1b[8;{screen_rows};{screen_cols}t')
time.sleep(0.1)

Deck = deck()
Deck.new_deck()

player1_hand = hand(Deck)

def main(stdscr):
    stdscr.clear()

    if curses.has_colors():
        curses.start_color()
    
    curses.init_pair(RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(BLUE_ON_BLACK, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(YELLOW_ON_BLACK, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(PURPLE_ON_BLACK, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(WHITE_ON_BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_color(Red_card, 940, 600, 600)

    player1_hand.print_hand(stdscr)

    stdscr.refresh()
    stdscr.getch()
    
wrapper(main)

