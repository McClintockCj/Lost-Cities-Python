import socket
import pickle
import curses
from curses import wrapper
from deck import deck

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 2000))

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

    stdscr.addstr(0, 0, "Connecting to server and receiving deck...")
    stdscr.refresh()
    time.sleep(0.5)
    data = client_socket.recv(3000)
    game_deck = pickle.loads(data)
    client = player(game_deck)
    time.sleep(0.5)
    status = pickle.loads(client_socket.recv(3000))
    if status == 1:
        client.player_num = 1
    else:
        client.player_num = 2
    print(parameter=stdscr, player=client, deck=game_deck)
    stdscr.clear()
    while game_deck.check_end():
        if (status == 1):
            stdscr.clear()
            if (client.player_num == 1):
                for i in range(3):
                    stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player1_string[i]))//2, player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
            else:
                for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player2_string[i]))//2, player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            client.turn(stdscr, game_deck)
            print(parameter=stdscr, player=client, deck=game_deck)
            status = 0
            time.sleep(0.5)
            client_socket.sendall(pickle.dumps(game_deck))
        if status == 0:
            stdscr.clear()
            if (client.player_num == 2):
                for i in range(3):
                    stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player1_string[i]))//2, player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
            else:
                for i in range(3):
                            stdscr.addstr(screen_rows//2 + i, (screen_cols - len(player2_string[i]))//2, player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))

            stdscr.refresh()
            time.sleep(0.5)
            data = client_socket.recv(3000)
            status = pickle.loads(data)
            time.sleep(0.5)
            data = client_socket.recv(3000)
            game_deck = pickle.loads(data)
    

try:
    wrapper(main)

except KeyboardInterrupt:
    client_socket.close()

except EOFError:
    client_socket.close()
