import curses
import threading
import socket
import pickle
import time
from player import player, screen_rows, screen_cols
from deck import deck
from card import RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK, YELLOW_ON_BLACK, PURPLE_ON_BLACK, WHITE_ON_BLACK


class Game_Type:
    Pass_and_Play = 1
    Host = 2
    Join = 3

def run_server():
    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("127.0.0.1", 2000))

        server_socket.listen(2)

        #print("Server is listening for connections...")
        (Player1, p1address) = server_socket.accept()
        #print(f"Connection from {p1address} has been established! Player 1 ready")
        (Player2, p2address) = server_socket.accept()
        #print(f"Connection from {p2address} has been established! Player 2 ready")
        #print("Ready to receive data from the client.")
        Deck = deck()
        Deck.new_deck()
        try:
            #print("Starting the game...")
            #print("sending deck to players")
            time.sleep(0.5)
            Player1.sendall(pickle.dumps(Deck))
            time.sleep(0.5)
            Player1.sendall(pickle.dumps(1))
            time.sleep(0.5)
            Player2.sendall(pickle.dumps(Deck))
            time.sleep(0.5)
            Player2.sendall(pickle.dumps(0))
            #print("Deck sent to players successfully.")

            while Deck.check_end():
                time.sleep(0.5)
                data = Player1.recv(3000)
                Deck = pickle.loads(data)
                time.sleep(0.5)
                Player2.sendall(pickle.dumps(1))
                time.sleep(0.5)
                Player2.sendall(pickle.dumps(Deck))

                time.sleep(0.5)
                data = Player2.recv(3000)
                Deck = pickle.loads(data)
                time.sleep(0.5)
                Player1.sendall(pickle.dumps(1))
                time.sleep(0.5)
                Player1.sendall(pickle.dumps(Deck))
        except:
            server_socket.close()

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
                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.self.player1_string[i]))//2, self.self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
            self.parameter.refresh()
            self.parameter.getch()

            print(self.parameter, player1, Deck)
            player1.turn(self.parameter, Deck)
            self.parameter.refresh()
            self.parameter.clear()

            for i in range(3):
                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.self.player2_string[i]))//2, self.self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
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
        self.parameter.clear()
        server_thread = threading.Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()
        self.parameter.addstr(screen_rows//2, (screen_cols - len("Server started. Waiting for players to join..."))//2, "Server started. Waiting for players to join...", curses.A_BOLD | curses.color_pair(GREEN_ON_BLACK))
        self.parameter.refresh()
        time.sleep(2)
        self.parameter.clear()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 2000))

        self.parameter.addstr(0, 0, "Connecting to server and receiving deck...")
        self.parameter.refresh()
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
        self.parameter.clear()
        while game_deck.check_end():
            if (status == 1):
                self.parameter.clear()
                if (client.player_num == 1):
                    for i in range(3):
                        self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player1_string[i]))//2, self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
                else:
                    for i in range(3):
                                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player2_string[i]))//2, self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
                self.parameter.refresh()
                time.sleep(2)
                self.parameter.clear()
                client.turn(self.parameter, game_deck)
                status = 0
                time.sleep(0.5)
                client_socket.sendall(pickle.dumps(game_deck))
            if status == 0:
                self.parameter.clear()
                if (client.player_num == 2):
                    for i in range(3):
                        self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player1_string[i]))//2, self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
                else:
                    for i in range(3):
                                self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player2_string[i]))//2, self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))

                self.parameter.refresh()
                time.sleep(0.5)
                data = client_socket.recv(3000)
                status = pickle.loads(data)
                time.sleep(0.5)
                data = client_socket.recv(3000)
                game_deck = pickle.loads(data)

    def Join(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("127.0.0.1", 2000))

            self.parameter.addstr(0, 0, "Connecting to server and receiving deck...")
            self.parameter.refresh()
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
            self.parameter.clear()
            while game_deck.check_end():
                if (status == 1):
                    self.parameter.clear()
                    if (client.player_num == 1):
                        for i in range(3):
                            self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player1_string[i]))//2, self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
                    else:
                        for i in range(3):
                                    self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player2_string[i]))//2, self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))
                    self.parameter.refresh()
                    time.sleep(2)
                    self.parameter.clear()
                    client.turn(self.parameter, game_deck)
                    status = 0
                    time.sleep(0.5)
                    client_socket.sendall(pickle.dumps(game_deck))
                if status == 0:
                    self.parameter.clear()
                    if (client.player_num == 2):
                        for i in range(3):
                            self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player1_string[i]))//2, self.player1_string[i], curses.A_BOLD | curses.color_pair(RED_ON_BLACK))
                    else:
                        for i in range(3):
                                    self.parameter.addstr(screen_rows//2 + i, (screen_cols - len(self.player2_string[i]))//2, self.player2_string[i], curses.A_BOLD | curses.color_pair(BLUE_ON_BLACK))

                    self.parameter.refresh()
                    time.sleep(0.5)
                    data = client_socket.recv(3000)
                    status = pickle.loads(data)
                    time.sleep(0.5)
                    data = client_socket.recv(3000)
                    game_deck = pickle.loads(data)
        except:
             client_socket.close()