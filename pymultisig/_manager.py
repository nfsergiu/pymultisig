import multiprocessing
import threading
import time

from ._util import _MetaBorg


class Manager(metaclass=_MetaBorg):
    is_init = False

    def __init__(self, pid=None, pipe: multiprocessing.connection.Connection = None):
        Manager.is_init = True
        print("Manager.__init__")
        self._subprocs = {}
        self._pid = pid
        self._pipe = pipe

        self._thread = threading.Thread(target=self._event_loop)
        self._thread.start()

    def _event_loop(self):
        # TODO
        while True:
            if self._pipe.poll():
                msg = self._pipe.recv()
