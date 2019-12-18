import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)

sock.connect(server_address)

try:
    # # Send data
    # message = 'e_i'
    # print('sending "%s"' % message)
    # payload = bytes(message, 'utf-8')
    # sock.sendall(payload)

    # # Look for the response
    # data = sock.recv(100)
    # print('received "%s"' % data)


    # send second data
    message = 'E_i'
    print('sending "%s"' % message)
    payload = bytes(message, 'utf-8')
    sock.sendall(payload)

    # Look for the response
    data = sock.recv(100)
    print('received "%s"' % data)


    message = 'E_Esc'
    print('sending "%s"' % message)
    payload = bytes(message, 'utf-8')
    sock.sendall(payload)

    # Look for the response
    data = sock.recv(100)
    print('received "%s"' % data)

    message = 'E_i'
    print('sending "%s"' % message)
    payload = bytes(message, 'utf-8')
    sock.sendall(payload)

    # Look for the response
    data = sock.recv(100)
    print('received "%s"' % data)


finally:
    print('closing socket')
    sock.close()