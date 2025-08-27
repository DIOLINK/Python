class ProgramUtil:
    def __init__(self):
        self.EXIT = True
        self.MESSAGES = []

    def init(self, *messajes):
        self.MESSAGES = list(messajes)
