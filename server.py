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
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying")
        socket_bind()


# Establish a connection with client(socket must be Listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established + " + "IP" +
          address[0] + "| PORT " + str(address[1]))
    send_commands(conn)
    conn.close()


