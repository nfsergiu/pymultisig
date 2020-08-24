

class Signal:
    def __init__(self, slots=None):
        # self.slots = slots if slots else self.slots = []
        pass
    def connect(self, slot):
        self.slots.append(slot)