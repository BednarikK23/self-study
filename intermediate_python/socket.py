# https://docs.python.org/3/library/socket.html?highlight=socket#module-socket
import socket

# sockets - bascally endpoints for network communication
# udp is faster, tcp i more secure so we have to choose

if __name__ == '__main__':
    # first arg specifies what kind of socket we want - we want internet socket now...
    # other address families:  (see link on line 1)
    # AF_UNIX -> bound to file system
    # AF_INET6
    # AF_NETLINK ...
    # snd argument - choosing tcp, cause we gonna send messages. other sovket types
    # socket.SOCK_DGRAM
    # socket.SOCK_RAW
    # socket.SOCK_RDM
    # socket.SOCK_SEQPACKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 55555))
    s.listen()

    while True:
        client, address = s.accept()
        print("Connected to {}".format("address"))
        client.send("You are connected!".encode())
        client.close()



