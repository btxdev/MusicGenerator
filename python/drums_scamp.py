from scamp import *
import random

s = Session(tempo=130)

drums = s.new_midi_part("drums", 1)
piano = s.new_midi_part("piano", 2)

def play_drums():
    for i in range(8):
        if i % 2 == 0:
            drums.play_note(36, 1, 0.5)
        else:
            drums.play_note(37, 1, 0.5)
        
def play_piano():
    for i in range(4):
        piano.play_note(36 + i * 2, 1, 0.25)            
                
while True:
    s.fork(play_drums)
    s.fork(play_piano)
    s.wait_for_children_to_finish()