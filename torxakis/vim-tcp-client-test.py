import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)

sock.connect(server_address)

try:
    message = 'E_i;test123'
    print('sending "%s"' % message)
    payload = bytes(message, 'utf-8')
    sock.sendall(payload)

    # Look for the response
    data = sock.recv(100)
    print('received "%s"' % data)

    message = 'E_O;lolo123'
    print('sending "%s"' % message)
    payload = bytes(message, 'utf-8')
    sock.sendall(payload)

    # Look for the response
    data = sock.recv(100)
    print('received "%s"' % data)


finally:
    print('closing socket')
    sock.close()