from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope


class InputEnvelope(BaseInputEnvelope):

    def __init__(self, walls, black, checkpoint, *flags):
        super().__init__(walls, *flags)
        self.black = black
        self.checkpoint = checkpoint


class OutputEnvelope(BaseOutputEnvelope):

    def __init__(self, direction, ignore, drop, *flags):
        super().__init__(direction, *flags)
        self.ignore = ignore
        self.drop = drop
