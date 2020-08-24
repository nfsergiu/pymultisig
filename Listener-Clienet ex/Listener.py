from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

while True:
    with Listener(address, authkey=b'secret password') as listener:
        with listener.accept() as conn:
            print('connection accepted from', listener.last_accepted)

            print(conn.recv())                  # => [2.25, None, 'junk', float]

            print(conn.recv_bytes())            # => 'hello'

            arr = array('i', [0, 0, 0, 0, 0])
            print(conn.recv_bytes_into(arr))    # => 8
            print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

