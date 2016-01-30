# CodeReclaimers LLC, Colbert GA 30628
# Copyright (c) 2016
# Distributed under the MIT license.

import time
import subprocess
from gtp import GoTextPipe, GoTextNetwork


def check(go):
    for _ in range(2):
        print(repr(go.genmove('black')))
        print(repr(go.genmove('white')))
        print(repr(go.estimate_score()))
        print(go.showboard())

    print(repr(go.boardsize(5)))
    print(repr(go.clear_board()))
    print(go.showboard())
    print(repr(go.play('black', 'A5')))
    print(repr(go.play('white', 'A4')))
    print(repr(go.estimate_score()))
    print(go.showboard())

    go.close()


def test_pipe():
    go = GoTextPipe()
    check(go)


def test_network():
    # Start an instance of gnugo.
    cmd = "gnugo --mode gtp --gtp-listen 127.0.0.1:50001 --boardsize 9"
    p = subprocess.Popen(cmd.split())
    time.sleep(1)

    go = GoTextNetwork('localhost', 50001)
    check(go)

    # Stop the gnugo instance.
    p.kill()
