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
    '4': 4,
    '2': 2,
    '1': 1,
    '8': 0.5,
    '16': 0.25,
    '32': 0.125,
    '64': 0.0625,
    '4.': 6,
    '2.': 3,
    '1.': 1.5,
    '8.': 0.75,
    '16.': 0.375,
    '32.': 0.1875,
    '64.': 0.09375,
    '4t': 2.6666666,
    '2t': 1.3333333,
    '1t': 0.6666666,
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

def get_pitch_from_values(key, octave):
    return int((octave * 12) + KEYS.index(key))

def get_pitch_from_str(str_note):
    octave = int(str_note[-1:])
    key = str_note[:-1].upper()
    return get_pitch_from_values(key, octave)

def get_note_value_from_str(value_str):
    return NOTE_VALUES[value_str]
