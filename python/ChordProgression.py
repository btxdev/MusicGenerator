import random

class ChordProgressionClass(object):
    def __init__(self, notes=(), novelty=0):
        self.progression = notes
        self.novelty = novelty

PROGRESSIONS = (
    ChordProgressionClass(notes=('1', '5', '6', '4'), novelty=0.0),
    ChordProgressionClass(notes=('1', '5', '6', '3', '4'), novelty=0.0),
    ChordProgressionClass(notes=('6', '5', '4', '5'), novelty=0.0),
    ChordProgressionClass(notes=('1', '6', '4', '5'), novelty=0.1),
    ChordProgressionClass(notes=('1', '5', '6', '5'), novelty=0.2),
    ChordProgressionClass(notes=('1', '5', '4', '5'), novelty=0.0),
    ChordProgressionClass(notes=('6', '4', '1', '3'), novelty=0.0),
    ChordProgressionClass(notes=('1', '1', '6', '5'), novelty=0.1),
    ChordProgressionClass(notes=('8', '7#', '6', '5'), novelty=0.1),
    ChordProgressionClass(notes=('1', '1', '6', '7'), novelty=0.5),
    ChordProgressionClass(notes=('6', '6', '8', '7'), novelty=0.3),
    ChordProgressionClass(notes=('3', '2', '1', '6'), novelty=0.3),
    ChordProgressionClass(notes=('1', '6', '4', '1#'), novelty=0.5),
    ChordProgressionClass(notes=('1', '4#', '4', '3'), novelty=0.4)
)

def RANDOM():
    return PROGRESSIONS[random.randint(0, len(PROGRESSIONS))]

    # ChordProgressionClass(notes=('1', '5', '6', '4'), novelty=0.0),
    # ChordProgressionClass(notes=('1', '5', '6', '3', '4'), novelty=0.0),
    # ChordProgressionClass(notes=('6', '5', '4', '5'), novelty=0.0),
    # ChordProgressionClass(notes=('1', '6', '4', '5'), novelty=0.1),
    # ChordProgressionClass(notes=('1', '5', '6', '5'), novelty=0.2),
    # ChordProgressionClass(notes=('1', '5', '4', '5'), novelty=0.0),
    # ChordProgressionClass(notes=('4', '2', '1.64', '5', '1'), novelty=0.4),
    # ChordProgressionClass(notes=('1', '5.6', '6', '6', '5'), novelty=0.2),
    # ChordProgressionClass(notes=('1', '2.7', '1.6', '4'), novelty=0.3),
    # ChordProgressionClass(notes=('1', '3.64', '6', '4'), novelty=0.1),
    # ChordProgressionClass(notes=('4', '1.6', '5'), novelty=0.4),
    # ChordProgressionClass(notes=('4', '1.6', '2'), novelty=0.5),
    # ChordProgressionClass(notes=('4', '5', '5.6/6', '6'), novelty=0.2),
    # ChordProgressionClass(notes=('1', '5/6', '6'), novelty=0.0),
    # ChordProgressionClass(notes=('6', '6.42', '4'), novelty=0.6),
    # ChordProgressionClass(notes=('1', '5.7/4', '4'), novelty=0.7),
    # ChordProgressionClass(notes=('5', '7.0/6', '6'), novelty=0.8),
    # ChordProgressionClass(notes=('4', '4', '1'), novelty=0.01),
    # ChordProgressionClass(notes=('1', '7b', '4', '1'), novelty=0.01),
    # ChordProgressionClass(notes=('1', '6b', '5'), novelty=0.01),
    # ChordProgressionClass(notes=('1', '5', '4', '7b', '1'), novelty=0.01),