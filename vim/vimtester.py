import re, pexpect, os

from pyte import ByteStream, Screen

TIMEOUT = pexpect.TIMEOUT

class VimTester(object):
    def __init__(self, PS1_re, any_PS_re, options, filename):
        self.PS1_re = PS1_re #re.compile(PS1_re)
        self.any_PS_re = any_PS_re #re.compile(any_PS_re)

        self._spawn_interpreter('vim ' + filename, options)
        self.options = options

        self.last_output = []

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
        for chunk in chunks:
            #print(chunk)
            self._stream.feed(chunk)

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
    
    def getScreenContent(self, expectedValue=None):
        waitingFor = [self.PS1_re, TIMEOUT, 'E325: ATTENTION']
        timeout = self.options['timeout']
        if(expectedValue is not None):
            waitingFor[0] = expectedValue
        PS_found, Timeout, ALREADY_OPEN = range(len(waitingFor))
        what = self.interpreter.expect(waitingFor, timeout=timeout)

        if what == ALREADY_OPEN:
            msg = "The Vim file is already openened, remove the swap file\n%s"
            msg = msg % ''.join(self.last_output)[-1000:]
            raise Exception(msg)
        if what == Timeout:
            msg = "Prompt not found: the code is taking too long to finish or there is a syntax error.\nLast 1000 bytes read:\n%s"
            msg = msg % ''.join(self.last_output)[-1000:]
            raise Exception(msg)
    
        self.last_output.append(self.interpreter.before)

        out = self._emulate_ansi_terminal(self.last_output)
        print (self.last_output)
        # self._drop_output()
        return out

    def _drop_output(self):
        self.last_output = []

