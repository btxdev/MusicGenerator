import random
import Key

class ScaleClass(object):

    def __init__(self, name, notes, novelty):
        self.name = name
        scale = ''
        for key in Key.KEYS:
            if key in notes:
                scale += '*'
            else:
                scale += '-'
        self.scale = scale
        self.novelty = novelty

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
    'major': ScaleClass('major', ('C','D','E','F','G','A','B'), 0),
    'pentatonic_major': ScaleClass('pentatonic_major', ('C','D','E','G','A'), 0.1),
    'blues_major': ScaleClass('blues_major', ('C','D#','F','F#','G','A'), 0.5),
    'minor': ScaleClass('minor', ('C','D','D#','F','G','G#','A#'), 0.2),
    'melodic_minor': ScaleClass('melodic_minor', ('C','D','D#','F','G','A','B'), 0.2),
    'harmonic_minor': ScaleClass('harmonic_minor', ('C','D','D#','F','G','G#','B'), 0.4),
    'pentatonic_minor': ScaleClass('pentatonic_minor', ('C','D#','F','G','A#'), 0.1),
    'blues_minor': ScaleClass('blues_minor', ('C','D#','F','F#','G','A#'), 0.3),
    'chromatic': ScaleClass('chromatic', ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B'), 1),
    'spanish': ScaleClass('spanish', ('C','C#','E','F','G','G#','A#'), 0.6),
    'jewish': ScaleClass('jewish', ('C','C#','E','F','G','G#','A#'), 0.7),
    'ionian': ScaleClass('ionian', ('C','D','E','F','G','A','B'), 0.3),
    'dorian': ScaleClass('dorian', ('C','D','D#','F','G','A','A#'), 0.3),
    'phrygian': ScaleClass('phrygian', ('C','C#','D#','F','G','G#','A#'), 0.6),
    'lydian': ScaleClass('lydian', ('C','D','E','F#','G','A','B'), 0.5),
    'mixolydian': ScaleClass('mixolydian', ('C','D','E','F','G','A','A#'), 0.4),
    'aeolian': ScaleClass('aeolian', ('C','D','D#','F','G','G#','A#'), 0.5),
    'locrian': ScaleClass('locrian', ('C','C#','D#','F','F#','G#','A#'), 0.5),
    'jazz_minor': ScaleClass('jazz_minor', ('C','D','D#','F','G','A','B'), 0.3),
    'major_arpeggio': ScaleClass('major_arpeggio', ('C','E','G'), 0.1),
    'minor_arpeggio': ScaleClass('minor_arpeggio', ('C','D#','G'), 0.4),
    'augmented_arpeggio': ScaleClass('augmented_arpeggio', ('C','E','G#'), 0.8),
    'diminished_arpeggio': ScaleClass('diminished_arpeggio', ('C','D#','F#','A'), 0.9)
}

def random_scale():
    return SCALES[random.randint(0, len(SCALES)-1)]