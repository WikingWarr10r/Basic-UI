class Ptr:
    def __init__(self, value=None):
        self.value = value

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"