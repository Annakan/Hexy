class HexyError(Exception):
    pass

class HexExistsError(HexyError):
    pass


class IncorrectCoordinatesError(HexyError):
    pass


class MismatchError(HexyError):
    pass

class NoIndexerForMap(HexyError):
    pass
