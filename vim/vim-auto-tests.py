import pexpect
child = pexpect.spawn ('vim tstst12e.txt')
child.send("i")
i = child.expect(r'.*INSERT.*')
child.send("een stukje tekst om te testen")
i = child.expect([pexpect.TIMEOUT, r'.*een stukje tekst om te testen.*'])
child.sendcontrol("c")
child.sendline(":wq")
i = child.expect([r'.*written.*'])
print i
