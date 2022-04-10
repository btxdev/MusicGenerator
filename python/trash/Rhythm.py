class RhythmClass(object):
    def __init__(self, rhythm_type):
        self.type = rhythm_type

STRAIGHT = RhythmClass('straight')
DOTTED = RhythmClass('dotted')
UPBEAT = RhythmClass('upbeat')
BACKBEAT = RhythmClass('backbeat')
SYNCOPE = RhythmClass('syncope')
LOMBARD = RhythmClass('lombard')