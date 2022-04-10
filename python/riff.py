import random

import Player
import Scale
import Key
import MelodicPattern
import Utils
import Note
from Tabulature import TabulatureClass

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
    

if __name__ == '__main__':

    scale1 = Scale.SCALES['jewish']
    key = 'B'
    key_note = Key.note(key, 2)

    guitar_tabs = Tabulature.Tabulature(8, 16)
    drum_tabs = Tabulature.Tabulature(8, 16)

    generate_drums(drum_tabs)

    player = Player.PlayerClass(140)

    player.create_channel('drums')
    player.create_channel('guitar')

    player.play(drum_tabs, 'drums')
    player.play(guitar_tabs, 'guitar')

    player.sync()