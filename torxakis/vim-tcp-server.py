import socket
import sys
import os 
import time
from vimtester import VimTester, TIMEOUT

# TCP server setup
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

# Vim tester setup
options = {}
options['geometry'] = (25, 100)
options['timeout'] = 2

testFileName = './tempfiles/test.txt'
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

def listen_for_connection():
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, testFileName)
            print('connection from', client_address)

            while True:
                data = connection.recv(100)
                if not data:
                    break
                decoded_data = bytes.decode(data)
                decoded_data = decoded_data.strip("\n")
                print('received "%s"' % decoded_data)

                separated_data = decoded_data.split(";")
                to_send = ""
                if len(separated_data) == 2:
                    cmd = separated_data[0]
                    txt = separated_data[1]

                    handle_currentElement(cmd, tester)
                    state = tester.getScreenContent()

                    handle_text(txt, tester)
                    handle_currentElement("E_Esc", tester)
                    handle_currentElement("E_W", tester)

                    file_content = read_temp_file()
                    print("file contains: %s" % file_content)
                    clean_temp_file(tester)
                    to_send = state + ";" + file_content + "\n"
                else:
                    to_send = "error"
                print("sending", to_send)
                connection.sendall(bytes(to_send, 'utf-8'))
                print("sent", to_send)
                
        finally:
            # Clean up the connection
            connection.close()
            shutdown(tester)


def handle_currentElement(ce, tester):
    print("Handle", ce)
    if ce == "E_CtrlC":
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
    elif ce == "E_W":
        tester.interpreter.sendline(":w")
    elif ce == "E_WQ":
        tester.interpreter.sendline(":w")
        time.sleep(0.1)
        tester.interpreter.sendline(":q!")
    else:
        print("Unknown action or state", ce)
    time.sleep(0.1)


def handle_text(txt, tester):
    if len(txt) != 0:
        tester.interpreter.send(txt)
        time.sleep(0.1)


def read_temp_file():
    f = open(testFileName, "r")
    txt = f.read().strip("\n")
    f.close()
    return txt


def clean_temp_file(tester):
    tester.interpreter.sendcontrol("c")
    time.sleep(0.1)
    tester.interpreter.sendline(":gg")
    time.sleep(0.1)
    tester.interpreter.sendline("dG")
    # open(testFileName, 'w').close()


def shutdown(tester):
    tester.interpreter.sendline(":w")
    time.sleep(0.1)
    tester.interpreter.sendline(":q!")

try:
    listen_for_connection()
finally:
    sock.close()