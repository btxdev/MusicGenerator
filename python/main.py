import Player
import Scale
import Key
import MelodicPattern
import random

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

def use_shred(scale, key_note):
    melody = []
    pattern1 = random.choice(MelodicPattern.PATTERNS_4)
    pattern2 = random.choice(MelodicPattern.PATTERNS_4)
    melody1 = use_pattern(scale, key_note, pattern1, pattern_shift=0)
    melody2 = use_pattern(scale, key_note, pattern1, pattern_shift=-1)
    melody3 = use_pattern(scale, key_note, pattern2, pattern_shift=0)
    melody4 = use_pattern(scale, key_note, pattern1, pattern_shift=2)
    melody = melody_in(melody, melody1)
    melody = melody_in(melody, melody2)
    melody = melody_in(melody, melody3)
    melody = melody_in(melody, melody4)
    return melody

def use_sweep(scale, key_note, size=3, dir='up', type=0):
    melody = []
    if size == 3:
        pass
    if size == 5:
        pass
    
    pattern = MelodicPattern.MelodicPatternClass()
    if type == 0:
        pattern.apply([1, 4, 7, 11, 14, 17])
    if type == 1:
        pattern.apply([1, 3, 6, 9, 11, 14])
    if type == 2:
        pass

def use_bend(note):
    pass

if __name__ == '__main__':

    

    scale1 = Scale.SCALES['jewish']
    scale2 = Scale.SCALES['spanish']
    key = 'F'
    key_note = Key.note(key, 3)

    shred1 = use_shred(scale1, key_note)
    shred2 = use_shred(scale1, key_note)
    shred3 = use_shred(scale2, key_note)

    song = []
    song = melody_in(song, use_bend(key_note))

    # song = melody_in(song, shred1)
    # song = melody_in(song, shred2)
    # song = melody_in(song, shred3)
    # song = melody_in(song, shred1)
    # song = melody_in(song, shred1)
    # song = melody_in(song, shred2)
    # song = melody_in(song, shred3)
    # song = melody_in(song, shred1)

    # song = melody_in(song, use_sweep(scale1, key_note))

    # for _ in range(40):
    #     volume = 1
    #     note = scale.get_note(key_note, 1)
    #     song.append([note, 0.45, volume])
    #     song.append([0, 0.05, volume])

    player = Player.PlayerClass(140)
    player.create_channel('piano')
    player.play(song, 'piano')