import socket
import threading

def main():
    host = '127.0.0.1'  # Localhost IP. The server is reachable only on the same machine.
    port = 8765

    # Create a socket instance to enable connections.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to a specific IP and port combination. It starts listening for connections on this address.
    server.bind((host, port))
    server.listen()

    print("Waiting for connection...")

    # Lists to store active clients and their corresponding nicknames for easy management and communication broadcasting.
    clients = []
    nicknames = []

    def broadcast(message, sender):
        # Broadcast a message to all connected clients except the sender.
        for client in clients:
            if client != sender:
                client.send(message)

    def handle(client):
        # Handle incoming messages from a client.
        while True:
            try:
                message = client.recv(1024).decode('utf-8')

                if message:
                    # Display the incoming message on the server terminal.
                    print(message)
                    # Broadcast the message to all clients.
                    broadcast(message.encode('utf-8'), client)
            except ConnectionResetError:
                print(f"A client disconnected: {client.getpeername()}")
                break
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                break

        # If a client disconnects or an error occurs, remove the client and close the connection.
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        broadcast(f'{nickname} left!'.encode('utf-8'), None)
        nicknames.remove(nickname)

    while True:
        # Accept a connection request from a client.
        client, address = server.accept()
        print(f"Connection established from {str(address)}")

        # Request the client's nickname and store it.
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Inform all connected clients of the new client.
        print(f'There is a new client. {nickname}!')
        broadcast(f'{nickname} joined!'.encode('utf-8'), None)
        client.send('Connected to server!'.encode('utf-8'))

        # Start a new thread to handle the client's incoming messages.
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()
