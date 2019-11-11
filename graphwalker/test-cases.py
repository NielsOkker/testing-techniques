from vimtester import VimTester, TIMEOUT
import time
import filecmp
from distutils.dir_util import copy_tree
import traceback
import os

options = {}
options['geometry'] = (25, 100)
options['timeout'] = 2

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
    
    tester.interpreter.send("gg")
    tester.interpreter.send("jj")
    
    tester.interpreter.send("a")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('ất cả mọi người sinh ra ều ược')
    tester.getScreenContent( r'ất cả mọi người sinh ra ều ược')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 4 Succeeded")
    else:
        print("Test 4 failed: result is not equal to the expected result") 

def test5():
    testFileName = 'test-5.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.interpreter.send("jj")
    
    tester.interpreter.send("A")
    tester.getScreenContent('INSERT')

    tester.interpreter.send( u'دا ستعمل نخذلكم')
    time.sleep(0.001)
    tester.getScreenContent(None)

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 5 Succeeded")
    else:
        print("Test 5 failed: result is not equal to the expected result") 

def test6():
    testFileName = 'test-6.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.interpreter.send("j")
    
    tester.interpreter.send("o")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Sed ut perspiciatis unde omnis')
    tester.getScreenContent( r'Sed ut perspiciatis unde omnis')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 6 Succeeded")
    else:
        print("Test 6 failed: result is not equal to the expected result") 

def test7():
    testFileName = 'test-7.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("O")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('00000000: 4e65 7665 7220 676f 6e6e 6120 6c65 7420')
    tester.getScreenContent( r'00000000: 4e65 7665 7220 676f 6e6e 6120 6c65 7420')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)
    
    tester.interpreter.sendline(":%!xxd -r")
    tester.getScreenContent('Never gonna let you down.')   
    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 7 Succeeded")
    else:
        print("Test 7 failed: result is not equal to the expected result") 

def test8():
    testFileName = 'test-8.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")
    tester.interpreter.send("j")
    tester.getScreenContent("2")
    tester.interpreter.send("gI")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Sed ut perspiciatis unde omnis')
    tester.getScreenContent( r'Sed ut perspiciatis unde omnis')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 8 Succeeded")
    else:
        raise Exception("Test 8 failed: result is not equal to the expected result")

def test9():
    testFileName = 'test-9.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")
    tester.interpreter.send("i")
    tester.getScreenContent('INSERT')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.send("jj")
    tester.getScreenContent("3")

    tester.interpreter.send("gi")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Lorem ipsum dolor sit amet.')
    tester.getScreenContent( r'Lorem ipsum dolor sit amet.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 9 Succeeded")
    else:
        raise Exception("Test 9 failed: result is not equal to the expected result")

def test10():
    testFileName = 'test-10.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")
    tester.interpreter.send("2s")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Hello world!')
    tester.getScreenContent( r'Hello world!')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 10 Succeeded")
    else:
        raise Exception("Test 10 failed: result is not equal to the expected result")

def test11():
    testFileName = 'test-11.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")
    tester.interpreter.send("3S")
    tester.getScreenContent('INSERT')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 11 Succeeded")
    else:
        raise Exception("Test 11 failed: result is not equal to the expected result")

def test12():
    testFileName = 'test-12.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")

    tester.interpreter.send("lll")
    tester.interpreter.send("C")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Testing yes 123.')
    tester.getScreenContent( r'Testing yes 123.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 12 Succeeded")
    else:
        raise Exception("Test 12 failed: result is not equal to the expected result")

def test13():
    testFileName = 'test-13.txt'
    tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, tempFolder + testFileName)
    
    tester.interpreter.send("gg")
    tester.getScreenContent("1,1")

    tester.interpreter.send("jj")
    tester.interpreter.send("cc")
    tester.getScreenContent('INSERT')

    tester.interpreter.send('Some text.')
    tester.getScreenContent( r'Some text.')

    tester.interpreter.sendcontrol("c")
    tester.getScreenContent(None)

    tester.interpreter.sendline(":w")
    tester.interpreter.sendline(":q")

    res = filecmp.cmp(tempFolder + testFileName, resultFolder + testFileName)
    
    if res:
        print("Test 13 Succeeded")
    else:
        raise Exception("Test 13 failed: result is not equal to the expected result")

try:
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()

except Exception as identifier:
    print("tests failed")
    traceback.print_exc()
    print(identifier)


test = os.listdir(tempFolder)

for item in test:
    if item.endswith(".swp"):
        os.remove(os.path.join(tempFolder, item))