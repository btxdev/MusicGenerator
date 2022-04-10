import random

import Utils

KEYS = (
    'C',
    'C#',
    'D',
    'D#',
    'E',
    'F',
    'F#',
    'G',
    'G#',
    'A',
    'A#',
    'B'
)

def random_key():
    return random.choice(KEYS)

class KeyClass(object):

    def __init__(self, key=None):
        if key is None or str(key).lower() == 'random':
            key = self.random()
        else:
            key = str(key).upper()
            if key not in KEYS:
                raise ValueError('Wrong music key')
            else:
                self.key = key

    def random(self):
        key = random_key()
        self.key = random_key()
        return key

    def note(self, octave):
        return Utils.get_pitch_from_values(self.key, octave)