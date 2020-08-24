import time
import pymultisig


class Display(pymultisig.Movable):
    @pymultisig.slot
    def display(self, message):
        print(f"Displaying a message: {message}")


def main():
    process = pymultisig.Process(name="Process #1")
    obj = Display()
    obj.move_to(process=process)

    signal = pymultisig.Signal()
    signal.connect(obj.display)

    print("I am going to emit a signal for Display.display('test message').")
    signal.emit()
    print("The signal has been emitted!")


if __name__ == '__main__':
    main()