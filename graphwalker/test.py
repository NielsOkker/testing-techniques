import json
import subprocess

from vimtester import VimTester, TIMEOUT
import time
import filecmp
from distutils.dir_util import copy_tree
import traceback
import os

options = {}
options['geometry'] = (25, 100)
options['timeout'] = 2

tempFolder = './tempfiles/'

def dejsonfy(jsonArray):
    array = []
    for i in jsonArray:
        array.append(i['currentElementName'])
    return array

def handle_currentElement(ce, tester):
    print("Handle", ce)
    if ce == "v_Normal":
        tester.getScreenContent()
    elif ce == "v_Insert":
        tester.getScreenContent('INSERT')
    elif ce == "e_Ctrl-C":
        tester.interpreter.sendcontrol("c")
    elif ce == "e_Esc":
        tester.interpreter.sendcontrol("c")
    elif ce == "e_i":
        tester.interpreter.send("i")
    elif ce == "e_I":
        tester.interpreter.send("I")
    elif ce == "e_a":
        tester.interpreter.send("a")
    elif ce == "e_A":
        tester.interpreter.send("A")
    elif ce == "e_o":
        tester.interpreter.send("o")
    elif ce == "e_O":
        tester.interpreter.send("O")
    elif ce == "e_gI":
        tester.interpreter.send("gI")
    elif ce == "e_gi":
        tester.interpreter.send("gi")
    elif ce == "e_s":        
        tester.interpreter.send("2s") 
    elif ce == "e_S":        
        tester.interpreter.send("3S") 
    elif ce == "e_cc":
        tester.interpreter.send("cc")
    elif ce == "e_C":
        tester.interpreter.send("C")
    else:
        print("Unknown action or state", ce)


def run_graphwalker_test(name_of_model, typeoftest):
    gw_output = subprocess.check_output(['java', '-jar', 'graphwalker-cli-4.0.1.jar', 'offline', '-m', \
    name_of_model, typeoftest])

    element_strings = gw_output.splitlines()
    stateArray = []
    for element_string in element_strings:
        stateArray.append(json.loads(element_string)['currentElementName'])

    testFileName = 'test-4.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)

    for i in stateArray:
        handle_currentElement(i, tester)

    handle_currentElement("e_Ctrl-C", tester)
    handle_currentElement("v_Normal", tester)
    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    print("Succesfuly transitioned ")

run_graphwalker_test('undefined.json', '"quick_random(edge_coverage(100))"')