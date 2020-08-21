import multiprocessing


class Responder:
    def __init__(self):
        self.message = "yes"

    def loop(self, message):
        while True:
            print("Still in loop: " + message)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    responder = Responder()

    process = multiprocessing.Process(target=responder.loop, args=("yes, sir", ))
    process.start()
    process.join()
