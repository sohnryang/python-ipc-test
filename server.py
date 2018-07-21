#!/usr/bin/env python

""" server.py
"""

from multiprocessing.connection import Listener

address = ('localhost', 12345)
listener = Listener(address, authkey=b'pass')
conn = listener.accept()
print('connection accepted from {0}'.format(listener.last_accepted))

while True:
    msg = conn.recv()
    if msg is not None:
        print('got message: {0}'.format(msg))
        if msg == 'close':
            conn.close()
            break
listener.close()
