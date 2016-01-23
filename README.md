# gtp
Library to communicate with instances of GNU Go via stdin/stdout or sockets.

# Example usage

    >>> import gtp
    >>> go = gtp.GoTextPipe()
    >>> go.genmove('black')
    'E5'
    >>> go.genmove('white')
    'C4'
    >>> print go.showboard()
    
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . O . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    >>> 

