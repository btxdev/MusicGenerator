import random
import classes.utils as utils

class Scale(object):

    def __init__(self, name, notes, novelty):
        scale = ''
        for key in utils.KEYS:
            if key in notes:
                scale += '*'
            else:
                scale += '-'

        self.name = name
        self.novelty = novelty
        self.scale = scale

    def get_note(self, start_note, at_degree):
        note = start_note
        current_degree = 0
        i = 0
        while True:
            if self.scale[i] == '*':
                current_degree += 1
            if at_degree == current_degree:
                return note
            note += 1
            i += 1
            if i > 11:
                i = 0

SCALES = {
    'major': Scale('major', ('C','D','E','F','G','A','B'), 0),
    'pentatonic_major': Scale('pentatonic_major', ('C','D','E','G','A'), 0.1),
    'blues_major': Scale('blues_major', ('C','D#','F','F#','G','A'), 0.5),
    'minor': Scale('minor', ('C','D','D#','F','G','G#','A#'), 0.2),
    'melodic_minor': Scale('melodic_minor', ('C','D','D#','F','G','A','B'), 0.2),
    'harmonic_minor': Scale('harmonic_minor', ('C','D','D#','F','G','G#','B'), 0.4),
    'pentatonic_minor': Scale('pentatonic_minor', ('C','D#','F','G','A#'), 0.1),
    'blues_minor': Scale('blues_minor', ('C','D#','F','F#','G','A#'), 0.3),
    'chromatic': Scale('chromatic', ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B'), 1),
    'spanish': Scale('spanish', ('C','C#','E','F','G','G#','A#'), 0.6),
    'jewish': Scale('jewish', ('C','C#','E','F','G','G#','A#'), 0.7),
    'ionian': Scale('ionian', ('C','D','E','F','G','A','B'), 0.3),
    'dorian': Scale('dorian', ('C','D','D#','F','G','A','A#'), 0.3),
    'phrygian': Scale('phrygian', ('C','C#','D#','F','G','G#','A#'), 0.6),
    'lydian': Scale('lydian', ('C','D','E','F#','G','A','B'), 0.5),
    'mixolydian': Scale('mixolydian', ('C','D','E','F','G','A','A#'), 0.4),
    'aeolian': Scale('aeolian', ('C','D','D#','F','G','G#','A#'), 0.5),
    'locrian': Scale('locrian', ('C','C#','D#','F','F#','G#','A#'), 0.5),
    'jazz_minor': Scale('jazz_minor', ('C','D','D#','F','G','A','B'), 0.3),
    'major_arpeggio': Scale('major_arpeggio', ('C','E','G'), 0.1),
    'minor_arpeggio': Scale('minor_arpeggio', ('C','D#','G'), 0.4),
    'augmented_arpeggio': Scale('augmented_arpeggio', ('C','E','G#'), 0.8),
    'diminished_arpeggio': Scale('diminished_arpeggio', ('C','D#','F#','A'), 0.9)
}

def random_scale():
    return random.choice(SCALES)