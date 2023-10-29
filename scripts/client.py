import socket
import threading

class ChatClient:
    def __init__(self, server_ip, server_port):
        # Initialize the ChatClient instance with the server IP and port.
        self.nickname = input("Choose your name: ")  # Get the user's chosen nickname.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket for the client.
        self.client.connect((server_ip, server_port))  # Connect to the server.

    def start(self):
        # Start two threads for receiving and sending messages.
        receive_thread = threading.Thread(target=self.receive_messages)
        send_thread = threading.Thread(target=self.send_messages)

        receive_thread.start()
        send_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                # Receive and decode messages from the server.

                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))  # Send the user's nickname to the server.
                else:
                    print(message)  # Print the received message to the user.
            except ConnectionResetError:
                print("The server closed the connection.")  # Handle a server connection reset.
                self.client.close()
                break
            except Exception as e:
                print(f"An error occurred: {str(e)}")  # Handle other exceptions.
                self.client.close()
                break

    def send_messages(self):
        while True:
            message = input()  # Get user input for sending messages.
            self.client.send(f'{self.nickname}: {message}'.encode('utf-8'))
# Send the message to the server.

def main():
    server_ip = '127.0.0.1'
    server_port = 8765

    chat_client = ChatClient(server_ip, server_port)  # Create a ChatClient instance.
    chat_client.start()  # Start the client.

if __name__ == "__main__":
    main()  # Run the chat client when the script is executed.
