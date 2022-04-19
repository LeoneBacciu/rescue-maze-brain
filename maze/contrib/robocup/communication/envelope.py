from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope, BaseHalfwayEnvelope


class InputEnvelope(BaseInputEnvelope):

    def __init__(self, walls, black, checkpoint, sides, *flags):
        super().__init__(walls, *flags)
        self.black = black
        self.checkpoint = checkpoint
        self.sides = sides


class OutputEnvelope(BaseOutputEnvelope):

    def __init__(self, direction, ignore, drop, *flags):
        super().__init__(direction, *flags)
        self.ignore = ignore
        self.drop = drop


class InputHalfwayEnvelope(BaseHalfwayEnvelope):
    def __init__(self, sides, *flags):
        super().__init__(sides, *flags)
        self.sides = sides


class OutputHalfwayEnvelope(BaseHalfwayEnvelope):
    def __init__(self, drop, *flags):
        super().__init__(drop, *flags)
        self.drop = drop
