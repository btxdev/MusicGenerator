class TabulatureClass():
    def __init__(self, tacts=8, precision=16):
        self.tabs = []
        self.tacts = tacts
        self.precision = precision
        if precision % 2 != 0:
            raise ValueError('parameter precision must be a multiple of 2, got value {} instead'.format(precision))
        # precision - how many parts contains in one tact
        for _ in range(tacts):
            for _ in range(precision):
                self.tabs.append([])
        