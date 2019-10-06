from vimtester import VimTester, TIMEOUT
import time
import filecmp
from distutils.dir_util import copy_tree
import traceback
import os

options = {}
options['geometry'] = (25, 100)
options['timeout'] = 1

inputFolder = './startfiles/'
resultFolder = './resultfiles/'
tempFolder = './tempfiles/'
copy_tree(inputFolder, tempFolder)

def test1():
    testFileName = 'test-1.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    tester.interpreter.send("i")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Lorem ipsum dolor sit amet.')
    tester.getScreenContent(r'Lorem ipsum dolor sit amet.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 1 Succeeded")
    else:
        print("Test 1 failed: result is not equal to the expected result")

def test2():
    testFileName = 'test-2.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    tester.interpreter.send("i")
    tester.getScreenContent('INSERT')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 2 Succeeded")
    else:
        print("Test 2 failed: result is not equal to the expected result")  
    
def test3():
    testFileName = 'test-3.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    tester.interpreter.send("i")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Lorem ipsum dolor sit amet.')
    tester.getScreenContent(r'Lorem ipsum dolor sit amet.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.send("I")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Museum ')
    tester.getScreenContent(r'Museum ')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 3 Succeeded")
    else:
        print("Test 3 failed: result is not equal to the expected result")  

def test4():
    testFileName = 'test-4.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    #tester.interpreter.send("j")
    
    tester.interpreter.send("a")
    tester.getScreenContent('INSERT')

    # tester.interpreter.send('ất cả mọi người sinh ra đều đượ.')
    tester.interpreter.send('teststring')
    tester.getScreenContent('teststring')

    tester.interpreter.sendline(":w")
    #tester.getScreenContent(None)
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 4 Succeeded")
    else:
        print("Test 4 failed: result is not equal to the expected result") 

try:
    test1()
    test2()
    test3()
    test4()
    
except Exception as identifier:
    print("tests failed")
    traceback.print_exc()
    print(identifier)


test = os.listdir(tempFolder)

for item in test:
    if item.endswith(".swp"):
        os.remove(os.path.join(tempFolder, item))