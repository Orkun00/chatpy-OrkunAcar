# TerminalChat

## Chat Application with Python

**Welcome to TerminalChat**, a simple chat application with Python. This application allows you to chat with others on your local machine using the terminal.

## Prerequisites

Before getting started, ensure that you have Python 3 installed. If you don't have Python 3, you can download it from the [official Python website](https://www.python.org/downloads) or install it on a Linux system using the following command:
   
      sudo apt update
      sudo apt install python3
## Setup and Usage

### Server Setup

**Open your terminal.**

**Navigate to the directory where `server.py` is located:**
   

      cd /path/to/your/directory

Start the server:



    python3 server.py

Client Setup

Open a new terminal window.

Navigate to the directory where client.py is located:


      cd /path/to/your/directory

Run the client:

    python3 client.py

Chatting

        Choose a nickname when prompted by the client.

        Start sending and receiving messages with other connected clients.

Security Considerations

!!  If you want this chat to be used by different devices you can go with 0.0.0.0 type of ip adress but it will be unsecure so be careful when using it  !! 

     Before you get started, please be aware of these security considerations:

      Lack of Encryption: Messages are not encrypted and may be intercepted. 
      Consider adding encryption for enhanced security.

      Denial of Service Vulnerabilities: This server is vulnerable to DoS attacks. 
      Implement rate limiting and request handling for production environments.

      No Authentication or Authorization: The system does not verify client identities. 
      Implement user authentication and authorization for enhanced security.

      Data Safety: Chat history can be viewed by anyone with access to a client's command line. 
      Consider implementing secure data storage and access control mechanisms for chat history.

Keep these security considerations in mind, and consider additional security measures for production or security-sensitive environments.

Enjoy chatting with TerminalChat!

