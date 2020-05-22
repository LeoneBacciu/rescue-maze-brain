
class MazeSettings:

    def __init__(self, matrix, cell, walls, dims, backup=False, backup_dir='./backup'):
        self.matrix = matrix
        self.cell = cell
        self.walls = walls
        self.dims = dims
        self.backup = backup
        self.backup_dir = backup_dir
