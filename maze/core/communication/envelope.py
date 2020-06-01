class Envelope:

    def __init__(self, data, flags=None):
        if flags is None:
            flags = []
        self.data = data
        self.flags = flags

    def split(self):
        return self.data, self.flags

    def __repr__(self):
        return f'Data: {self.data}, Flags: {self.flags}'
