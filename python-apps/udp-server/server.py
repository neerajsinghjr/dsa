"""
#---------------------------------#
UPD Client : 
#---------------------------------#
Know More : https://pythontic.com/modules/socket/udp-client-server-example

#---------------------------------#
SOCKET_AF_INET FAMILY
#---------------------------------#
AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket. 

The Linux kernel, for example, supports 29 other address families such as UNIX (AF_UNIX) sockets and IPX (AF_IPX), and also communications with IRDA and Bluetooth (AF_IRDA and AF_BLUETOOTH, but it is doubtful you'll use these at such a low level).

For the most part, sticking with AF_INET for socket programming over a network is the safest option. There is also AF_INET6 for Internet Protocol v6 addresses.

#---------------------------------#
SOCK_DGRAM AND SOCK_STREAM
#---------------------------------#
TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM.

TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.

UDP (SOCK_DGRAM) is a datagram-based protocol. You send one datagram and get one reply and then the connection terminates.

If you send multiple packets, TCP promises to deliver them in order. UDP does not, so the receiver needs to check them, if the order matters.

If a TCP packet is lost, the sender can tell. Not so for UDP.

UDP datagrams are limited in size, from memory I think it is 512 bytes. TCP can send much bigger lumps than that.

TCP is a bit more robust and makes more checks. UDP is a shade lighter weight (less computer and network stress).

"""

import socket


def run_udp_server():
    # udp client constants;;
    local_ip = '127.0.0.1'
    local_port = 2002
    buffer_size = 1024

    # create udp socket;;
    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind address with ip;;
    udp_server_socket.bind((local_ip, local_port))

    print("UDP Server is running ....")

    # listen to the port;;
    while(True):
        # message received;;
        raw_message = udp_server_socket.recvfrom(buffer_size)
        message, client_ip = raw_message
        print(f"Client saying: ", message.decode())

        # convert ascii to byte datagram;;
        message = input("Server Reply: ")
        enc_message = str.encode(message)

        # client will send message;;
        udp_server_socket.sendto(enc_message, client_ip)


if __name__ == "__main__":
    print("Starting UDP Server...")
    run_udp_server()
    print("Terminating UDP Server...")