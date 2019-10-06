from vimtester import VimTester, TIMEOUT
import time
import filecmp

options = {}
options['geometry'] = (25, 100)
options['timeout'] = 1

inputFolder = '../startfiles/'
resultFolder = '../resultfiles/'
tempFolder = '../tempfiles/'

def test1():
    testFileName = 'test-1.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, testFileName)
    tester.interpreter.send("i")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Lorem ipsum dolor sit amet.')
    tester.getScreenContent(r'Lorem ipsum dolor sit amet.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":wq")

    filecmp.cmp(inputFolder + testFileName, resultFolder + testFileName)

    print("tests succeeded")
    

try:
    test1()
    
except Exception as identifier:
    print("tests failed")
    print(identifier)


