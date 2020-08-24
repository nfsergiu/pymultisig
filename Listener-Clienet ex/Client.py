from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'secret password') as conn:

    conn.send([2.25, None, 'junk', float])

    conn.send_bytes(b'hello')

    conn.send_bytes(array('i', [42, 1729]))