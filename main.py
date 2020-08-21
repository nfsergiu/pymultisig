import multiprocessing


class Responder:
    def __init__(self):
        self.message = "yes"

    def respond(self):
        print("Response " + self.message)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    responder = Responder()

    process = multiprocessing.Process(target=responder.respond)
    process.start()
    process.join()
