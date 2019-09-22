import re, pexpect, os

from pyte import ByteStream, Screen

class VimTester(object):
    def __init__(self, PS1_re, any_PS_re):
        self.PS1_re = PS1_re #re.compile(PS1_re)
        self.any_PS_re = any_PS_re #re.compile(any_PS_re)

    def _create_terminal(self, options):
        rows, cols = options['geometry']

        self._screen = Screen(cols, rows)
        self._stream = ByteStream(self._screen)

    def _spawn_interpreter(self, cmd, options):
        rows, cols = options['geometry']
        self._terminal_default_geometry = (rows, cols)

        env = os.environ.copy()
        env.update({'LINES': str(rows), 'COLUMNS': str(cols)})

        self.interpreter = pexpect.spawn(cmd, echo=False, 
                                                dimensions=(rows,cols),
                                                env=env)

        self._create_terminal(options)

    def _emulate_ansi_terminal(self, chunks, join=True):
        #for chunk in chunks:
            #print(chunk)
        self._stream.feed(chunks)

        lines = self._screen.display
        self._screen.reset()
        if str == bytes:
            # Python 2.7 support only: it works on str/bytes only
            # XXX this is a limitation, if the output has a single non-ascii
            # character this will blow up without the 'ignore'
            lines = (str(line.rstrip().encode('ascii', 'ignore')) for line in lines)
        else:
            lines = (line.rstrip() for line in lines)

        return '\n'.join(lines) if join else lines

options = {}
options['geometry'] = (25, 100)
tester = VimTester(r'(All|Bot|Top|\d+\%)+', r'')
tester._spawn_interpreter('vim tezt', options)
tester.interpreter.send("i")
prompt_re = tester.PS1_re
expect = [prompt_re, pexpect.TIMEOUT]
i = tester.interpreter.expect(expect)
output = tester.interpreter.before
out = tester._emulate_ansi_terminal(output)
i=0
for line in out.split('\n'):
    print(str(i) + line)
    i=i+1


#child.send("een stukje tekst om te testen")
#i = child.expect([pexpect.TIMEOUT, r'.*een stukje tekst om te testen.*'])
#child.sendcontrol("c")
#child.sendline(":wq")
#i = child.expect([r'.*written.*'])
#print i
