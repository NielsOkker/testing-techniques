from vimtester import VimTester, TIMEOUT
import time

options = {}
options['geometry'] = (25, 100)
options['timeout'] = 100
tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'', options, 'test-1.txt')

tester.interpreter.send("i")
output = tester.getScreenContent('INSERT')
i=0
for line in output.split('\n'):
    print(str(i) + line)
    i=i+1
tester.interpreter.send('Lorem ipsum dolor sit amet.')
output = tester.getScreenContent(r'Lorem ipsum dolor sit amet.')
i=0
for line in output.split('\n'):
    print(str(i) + line)
    i=i+1
tester.interpreter.sendcontrol("c")
output = tester.getScreenContent(r'(All|Bot|Top|\d+\%)+')
i=0
for line in output.split('\n'):
    print(str(i) + line)
    i=i+1
tester.interpreter.sendline(":wq")