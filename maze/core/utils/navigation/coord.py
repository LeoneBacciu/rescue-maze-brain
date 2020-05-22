class Coord:

    def __init__(self, *args):
        if len(args) == 1:
            assert isinstance(args[0][0], int) and isinstance(args[0][1], int)
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            assert isinstance(args[0], int) and isinstance(args[1], int)
            self.x = args[0]
            self.y = args[1]

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(other.x+self.x, other.y+self.y)
        elif isinstance(other, tuple):
            return Coord(other[0]+self.x, other[1]+self.y)

    def __repr__(self):
        return f'x: {self.x}; y: {self.y}'

    def update(self, *args):
        self.__init__(*args)
