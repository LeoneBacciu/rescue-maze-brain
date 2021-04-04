class EncoderOverflowError(Exception):
    """Data overflow"""
    pass


class MissingDelimitersError(Exception):
    """Missing START or STOP tokens"""
    pass


class NoCellsMatch(Exception):
    pass


class StopExecution(Exception):
    pass
