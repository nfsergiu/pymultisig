import time
import pymultisig


class Display(pymultisig.Movable):
    @pymultisig.slot
    def display(self, message):
        print(f"Displaying a message: {message}")


def main():
    process = pymultisig.Process()
    process.start()
    obj = Display()
    obj.move_to(process=process)

    signal = pymultisig.Signal()
    signal.connect(slot=obj.display)

    print("I am going to emit a signal for Display.display('test message').")
    signal.emit()
    print("The signal has been emitted!")

    while True:
        print("MAIN")
        time.sleep(1)


if __name__ == '__main__':
    main()