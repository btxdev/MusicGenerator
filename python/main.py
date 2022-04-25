import random
import sys

from pathlib import Path
from scamp import *

import classes.utils as utils
from classes.tablature import Tablature
from classes.player import Player
from classes.note import Note
from classes.scale import SCALES
from classes.scale import Scale
from classes.midi import CreateMidiFile

DEBUG = False
SCRIPT_DIR = Path(__file__).parent.resolve()
MIDI_OUTPUT_PATH = Path(SCRIPT_DIR, '../midi/')

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

def generate_drums(type=0, tacts=2):

    tabs = Tablature(tacts=tacts, precision=32)

    if type in (0, 1, 2):
        # cymbals
        every_beat = tabs.precision // 4
        for tact in range(tabs.tacts):
            for beat in range(0, tabs.precision, every_beat):
                pos = (tact * tabs.precision) + beat
                tabs.paste(Note(utils.NOTE_VALUES['8'], utils.DRUMS['CHINA'], 1), pos)
        # kick and snare
        if type == 0:
            DRUM_PATTERNS = (
                '*-------',
                '----*---',
                '*---*---',
                '*---*-*-',
                '*-*-----',
                '*-*-*---',
                '*-*---*-'
            )
        if type == 1:
            DRUM_PATTERNS = (
                '*-*-*-*-',
                '*-*-*---',
                '*-*-----',
                '*-------'
            )
        if type == 2:
            DRUM_PATTERNS = (
                '*---*---',
                '----*---',
                '*-*-----'
            )
        patterns_count = len(tabs.tabs) // len(DRUM_PATTERNS[0])
        for j in range(patterns_count):
            drum_pattern = random.choice(DRUM_PATTERNS)
            for i in range(len(drum_pattern)):
                if(drum_pattern[i] == '*'):
                    pos = (i + j * len(DRUM_PATTERNS[0]))
                    if pos % 16 == 0 and pos % 32 != 0:
                        tabs.paste(Note(utils.NOTE_VALUES['32'], utils.DRUMS['SNARE'], 1), pos)
                    else:
                        tabs.paste(Note(utils.NOTE_VALUES['32'], utils.DRUMS['KICK'], 1), pos)
                else:
                    pass

    return tabs


def generate_guitar(tabs):
    # test
    every_beat = tabs.precision // 2
    for tact in range(tabs.tacts):
        for beat in range(0, tabs.precision, every_beat):
            pos = (tact * tabs.precision) + beat + 1
            tabs.paste(Note(utils.NOTE_VALUES['8'], utils.pitch_from_values('F', 4), 1), pos)
    return tabs

def tablature_to_midi(tablature, tempo, midi, channel):
    for note, time in tablature.get_notes(tempo):
        midi.add_note(channel, note, time)

if __name__ == '__main__':

    key = 'B'
    tempo = 120
    scale = SCALES['jewish']
    key_note = utils.pitch_from_values(key, octave=2)

    drum_tabs = generate_drums(type=2, tacts=8)

    # create midi files
    drum_midi = CreateMidiFile('Drums', tempo)

    # paste tablature
    tablature_to_midi(drum_tabs, tempo, drum_midi, 0)

    # save files
    drum_midi.save(MIDI_OUTPUT_PATH)