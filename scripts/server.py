import socket
import threading

# Server configuration
#Also if you want this chat to be used by different devices you can go with 0.0.0.0 type of ip adress but it will be unsecure so be careful when using it
host = '127.0.0.1'
port = 8765

# Creating a socket instance for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists to store active clients and their corresponding nicknames
clients = []
nicknames = []

# Function to broadcast a message to all connected clients and print it to the server terminal
def broadcast(message):
    for client in clients:
        client.send(message)
    print(message.decode('ascii'))  # Print the message to the server terminal

# Function to handle incoming messages from clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Main function to receive and manage incoming client connections
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start the server's main loop
print("Listening for incoming connections...")
receive()
