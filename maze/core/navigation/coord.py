class Coord:

    def __init__(self, *args):
        if len(args) == 1:
            assert isinstance(args[0], Coord)
            self.x = args[0].x
            self.y = args[0].y
        else:
            assert isinstance(args[0], int) and isinstance(args[1], int)
            self.x = args[0]
            self.y = args[1]

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Coord(other[0] + self.x, other[1] + self.y)

    def __sub__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple):
            return Coord(self.x - other[0], self.y - other[1])

    def __getitem__(self, item):
        if item < 0 or item > 1:
            raise IndexError
        return self.x if item == 0 else self.y

    def __repr__(self):
        return f'x: {self.x}; y: {self.y}'

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash(f'{self.x}{self.y}')

    def update(self, *args):
        self.__init__(*args)

    def get(self):
        return self.x, self.y


def absoluteToRelative(coords: list):
    out = []
    for i in range(1, len(coords)):
        out.append(coords[i] - coords[i - 1])
    return out
