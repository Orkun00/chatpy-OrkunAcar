import socket
import threading

# Choosing a nickname for the client
nickname = input("Choose your nickname: ")

# Creating the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the client socket to the server
client.connect(('127.0.0.1', 8765))

# Function to handle receiving messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Function to continuously prompt the user for input (messages to send)
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# After this create and start the receiving thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# After this create and start the writing thread
write_thread = threading.Thread(target=write)
write_thread.start()
