import socket
import pickle
from deck import deck
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 2000))

server_socket.listen(2)

print("Server is listening for connections...")
(Player1, p1address) = server_socket.accept()
print(f"Connection from {p1address} has been established! Player 1 ready")
(Player2, p2address) = server_socket.accept()
print(f"Connection from {p2address} has been established! Player 2 ready")
print("Ready to receive data from the client.")
Deck = deck()
Deck.new_deck()
try:
    print("Starting the game...")
    print("sending deck to players")
    time.sleep(0.5)
    Player1.sendall(pickle.dumps(Deck))
    time.sleep(0.5)
    Player1.sendall(pickle.dumps(1))
    time.sleep(0.5)
    Player2.sendall(pickle.dumps(Deck))
    time.sleep(0.5)
    Player2.sendall(pickle.dumps(0))
    print("Deck sent to players successfully.")

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
    
except KeyboardInterrupt:
    server_socket.close()

except EOFError:
    server_socket.close()