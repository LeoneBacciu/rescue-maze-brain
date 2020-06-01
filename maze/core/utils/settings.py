class MazeSettings:

    def __init__(self, map, matrix, cell, walls, dims, backup=False, backup_dir='./backup'):
        self.map = map
        self.matrix = matrix
        self.cell = cell
        self.walls = walls
        self.dims = dims
        self.backup = backup
        self.backup_dir = backup_dir


class SerialSettings:

    def __init__(self, bridge, port, baud_rate, flag):
        self.bridge = bridge
        self.port = port
        self.baud_rate = baud_rate
        self.flag = flag
