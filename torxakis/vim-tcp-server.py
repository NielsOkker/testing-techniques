import socket
import sys
import os 
from vimtester import VimTester, TIMEOUT

# TCP server setup
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

# Vim tester setup
options = {}
options['geometry'] = (25, 100)
options['timeout'] = 2

testFileName = './test.txt'
tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, testFileName)


print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

def listen_for_connection():
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(100)
                if not data:
                    break
                decoded_data = bytes.decode(data)
                decoded_data = decoded_data.strip("\n")
                print('received "%s"' % decoded_data)

                handle_currentElement(decoded_data, tester)
                state = tester.getScreenContent()
                connection.sendall(bytes(state + "\n", 'utf-8'))
                
                
        finally:
            # Clean up the connection
            connection.close()
            shutdown()


def handle_currentElement(ce, tester):
    print("Handle", ce)
    if ce == "E_Ctrl-C":
        tester.interpreter.sendcontrol("c")
    elif ce == "E_Esc":
        tester.interpreter.sendcontrol("c")
    elif ce == "E_i":
        tester.interpreter.send("i")
    elif ce == "E_I":
        tester.interpreter.send("I")
    elif ce == "E_a":
        tester.interpreter.send("a")
    elif ce == "E_A":
        tester.interpreter.send("A")
    elif ce == "E_o":
        tester.interpreter.send("o")
    elif ce == "E_O":
        tester.interpreter.send("O")
    elif ce == "E_gI":
        tester.interpreter.send("gI")
    elif ce == "E_gi":
        tester.interpreter.send("gi")
    elif ce == "E_s":        
        tester.interpreter.send("2s") 
    elif ce == "E_S":        
        tester.interpreter.send("3S") 
    elif ce == "E_cc":
        tester.interpreter.send("cc")
    elif ce == "E_C":
        tester.interpreter.send("C")
    else:
        print("Unknown action or state", ce)

def shutdown():
    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q!")

listen_for_connection()