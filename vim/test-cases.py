from vimtester import VimTester, TIMEOUT
import time
import filecmp
from distutils.dir_util import copy_tree


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
    
    
    

try:
    test1()
    
except Exception as identifier:
    print("tests failed")
    print(identifier)


