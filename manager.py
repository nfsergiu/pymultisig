from multiprocessing.connection import Listener
from constants import Constants


class Manager:
    def __init__(self, father=None):
        self.subprocesses = []
        self.father = father
        self.listener = Listener(address=Constants.address, authkey=Constants.password)
        self.connection = self.listener.accept()
        print('Connection accepted from ', self.listener.last_accepted)
        self.listen()

    def listen(self):
        try:
            while True:
                message = self.connection.recv()
                print(message)
        finally:
            self.listener.close()

    def decode(self, message):
        pass

    def new_slot(self, class_name, method):
        pass

    def register_slot(self, signal, slot):
        pass

    def emit(self, slot):
        pass
