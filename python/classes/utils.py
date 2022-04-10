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

NOTE_VALUES = {
    'x4': 4,
    'x2': 2,
    '4': 1,
    '8': 0.5,
    '16': 0.25,
    '32': 0.125,
    '64': 0.0625,
    'x4.': 6,
    'x2.': 3,
    '4.': 1.5,
    '8.': 0.75,
    '16.': 0.375,
    '32.': 0.1875,
    '64.': 0.09375,
    'x4t': 2.6666666,
    'x2t': 1.3333333,
    '4t': 0.6666666,
    '8t': 0.3333333,
    '16t': 0.1666666,
    '32t': 0.0833333,
    '64t': 0.0416666
}

DRUMS = {
    'KICK': 36,
    'SNARE': 38,
    'SNARE_RIM': 37,
    'TOM_1': 41,
    'TOM_2': 45 ,
    'TOM_3': 47,
    'TOM_4': 48,
    'HI_HAT_OPEN': 46,
    'HI_HAT_CLOSED': 42,
    'HI_HAT_PEDAL': 44,
    'CRASH': 49,
    'RIDE': 51,
    'BELL': 53,
    'CHINA': 52,
    'SPLASH': 55
}

def pitch_from_values(key, octave):
    return int((octave * 12) + KEYS.index(key))

def pitch_from_str(str_note):
    octave = int(str_note[-1:])
    key = str_note[:-1].upper()
    return pitch_from_values(key, octave)

def note_value_from_str(value_str):
    return NOTE_VALUES[value_str]

def random_key():
    return random.choice(KEYS)

def random_note_value(type='any', min=0, max=-1):
    if type == 'dotted':
        values = NOTE_VALUES[7:13]
    elif type == 'triplet':
        values = NOTE_VALUES[14:]
    else:
        values = NOTE_VALUES[:6]
    return random.choice(values[min:max])
