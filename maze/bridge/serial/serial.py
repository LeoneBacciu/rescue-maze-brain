from serial import Serial as PySerial


class Serial:

    def __init__(self, port, baud_rate, **kwargs):
        self.port = port
        self.baud_rate = baud_rate
        if 'timeout' not in kwargs.keys():
            kwargs.update({'timeout': None})
        self.serial = PySerial(port, baud_rate, **kwargs)

    def write(self, data):
        self.serial.write(data)

    def read(self):
        buffer = bytes()
        while len(buffer) == 0 or buffer[-1] != 0xff:
            buffer += self.serial.read(1)
        return buffer

    def __del__(self):
        # self.serial.close()
        pass
