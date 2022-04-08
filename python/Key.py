import random

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

def RandomKeyValue():
    return KEYS[random.randint(0, len(KEYS))]

class KeyClass(object):

    def __init__(self, key=None):
        if key is None or key == 'Random':
            key = self.set_random()
        else:
            if key not in KEYS:
                raise ValueError('Wrong music key')
            self.key = key

    def set_random(self):
        self.key = RandomKeyValue()
        return self.key

def Random():
    return KeyClass()