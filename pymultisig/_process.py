import multiprocessing
import os
import time

from ._manager import Manager


class Process(object):
    def __init__(self):
        self._pid = os.getpid()
        self._pipe, child_pipe = multiprocessing.Pipe(duplex=True)
        self._process = multiprocessing.Process(target=Manager,
                                                kwargs={"pid": self._pid,
                                                        "pipe": child_pipe})

    def start(self):
        self._process.start()
        self._pipe.send("MESAJ")