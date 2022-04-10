import random

SONG_BLOCK_TYPES = (
    'INTRO',
    'OUTRO',
    'VERSE',
    'PRE-CHORUS',
    'CHORUS',
    'BREAK',
    'BREAKDOWN'
)

class SongBlockClass(object):

    def __init__(self, type=None, tacts=None):
        # type
        if type is None or str(type).lower() == 'random':
            self.type = self.random()
        else:
            type = str(type).upper()
            if type not in SONG_BLOCK_TYPES:
                raise ValueError('Wrong song block name')
            else:
                self.type = type
        # tacts
        if tacts is None:
            if type == 'INTRO':
                tacts = 4
            if type == 'OUTRO':
                tacts = 8
            if type == 'VERSE':
                tacts = 16
            if type == 'CHORUS':
                tacts = 8
            if type == 'BREAKDOWN':
                tacts = 8
            if type == 'BRIDGE':
                tacts = 4
            if type == 'PRE-CHORUS':
                tacts = 8
        self.tacts = tacts

    def random(self):
        return SONG_BLOCK_TYPES[random.randint(0, len(SONG_BLOCK_TYPES))]

# INTRO = SongBlockClass('Intro')
# OUTRO = SongBlockClass('Outro')
# VERSE = SongBlockClass('Verse')
# PRE_CHORUS = SongBlockClass('Pre-Chorus')
# CHORUS = SongBlockClass('Chorus')
# BREAK = SongBlockClass('Break')
# BREAKDOWN = SongBlockClass('Breakdown')