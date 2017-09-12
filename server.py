import socket
import sys


# create socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        # allow computer to talk with another computer
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error: " + str(msg))


# bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to Port: " + str(port))
        s.bind((host, port))
        # allow server to accept connection
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying")
        socket_bind()


# Establish a connection with client(socket must be Listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established + " + "IP" + address[0] + "| PORT " + str(address[1]))
    send_commands(conn)
    conn.close()


# send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
