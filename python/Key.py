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

# def RandomKeyValue():
#     return KEYS[random.randint(0, len(KEYS))]

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
        return KEYS[random.randint(0, len(KEYS))]

# def Random():
#     return KeyClass()