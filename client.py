#!/usr/bin/env python

""" client.py
"""

from multiprocessing.connection import Client
import sys

address = ('localhost', 12345)
conn = Client(address, authkey=b'pass')
conn.send(sys.argv[1])
conn.close()
