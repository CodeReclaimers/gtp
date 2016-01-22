import socket
import subprocess

__all__ = ['FailedCommand', 'GoTextNetwork', 'GoTextPipe']


class FailedCommand(Exception):
    pass


class GoTextBase:
    def _send(self, data):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def genmove(self, color):
        return self._send('genmove {0}'.format(color)).strip()

    def estimate_score(self):
        return self._send('estimate_score').strip()

    def showboard(self):
        return self._send('showboard')


class GoTextNetwork(GoTextBase):
    """
    Communicate with an already running instance of gnugo over a socket.
    """
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def _send(self, data):
        self.sock.sendall('{0}\n'.format(data))
        result = []
        while 1:
            data = self.sock.recv(1024 * 1024)
            result.append(data)
            if '\n\n' in data:
                break
        result = ''.join(result)
        if result[0] == '?':
            raise FailedCommand(result)

        result = result[1:]
        return result

    def close(self):
        self.sock.close()
        self.sock = None


class GoTextPipe(GoTextBase):
    """
    Start a new instance of gnugo and communicate with it via stdin/stdout.
    """
    def __init__(self, board_size=9):
        args = 'gnugo --mode gtp --boardsize {0}'.format(board_size)
        self.gnugo = subprocess.Popen(args.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def _send(self, data):
        self.gnugo.stdin.write('{0}\n'.format(data))
        result = []
        while 1:
            data = self.gnugo.stdout.readline()
            if not data.strip():
                break
            result.append(data.rstrip())

        result = '\n'.join(result)
        if result[0] == '?':
            raise FailedCommand(result)

        return result[1:]

    def close(self):
        self.gnugo.communicate('quit\n')
        self.gnugo = None


