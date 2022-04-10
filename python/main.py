import random
import sys

from scamp import *

import classes.utils as utils
from classes.tablature import Tablature
from classes.player import Player
from classes.note import Note
from classes.scale import SCALES
from classes.scale import Scale

def pause_note(duration):
    return (0, duration, 0)

def melody_in(song, melody):
    for note in melody:
        song.append(note)
    return song

def use_pattern(scale, key_note, pattern, pattern_shift=0):
    if pattern_shift < 0:
        pattern_shift += 7
        key_note -= 12
    melody = []
    for i in pattern.pattern:
        degree = i + pattern_shift
        pitch = scale.get_note(key_note, degree)
        duration = 0.25
        pause_percent = 0.1
        pause = duration * pause_percent
        duration = duration - pause
        volume = 0.2
        note = (pitch, duration, volume)
        melody.append(note)
        melody.append(pause_note(pause))
    return melody

def generate_drums(tabs):
    # cymbals
    every_beat = tabs.precision // 4
    for tact in range(tabs.tacts):
        for beat in range(0, tabs.precision, every_beat):
            pos = (tact * tabs.precision) + beat
            tabs.paste(Note(utils.NOTE_VALUES['8'], utils.DRUMS['CHINA'], 1), pos)
    return tabs

def generate_guitar(tabs):
    # test
    every_beat = tabs.precision // 2
    for tact in range(tabs.tacts):
        for beat in range(0, tabs.precision, every_beat):
            pos = (tact * tabs.precision) + beat + 1
            tabs.paste(Note(utils.NOTE_VALUES['4'], utils.pitch_from_values('F', 4), 1), pos)
    return tabs

if __name__ == '__main__':

    scale = SCALES['jewish']
    key = 'B'
    key_note = utils.pitch_from_values(key, octave=2)

    drum_tabs = Tablature(tacts=8, precision=16)
    guitar_tabs = Tablature(tacts=8, precision=16)

    drum_tabs = generate_drums(drum_tabs)
    guitar_tabs = generate_guitar(guitar_tabs)

    #drum_tabs.print()

    player = Player(140)

    player.create_channel('drums')
    player.create_channel('guitar')

    player.play(drum_tabs, 'drums')
    player.play(guitar_tabs, 'guitar')
    player.sync()