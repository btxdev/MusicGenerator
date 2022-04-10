import random

import Rhythm
import SongBlock

class SongStructureClass():

    def __init__(self):
        self.chord_complexity = 0
        self.melodic_complexity = 0
        self.chord_melody_tension = 0
        self.chord_progression_novelty = 0
        self.rhythm_complexity = 1
        self.rhythm = Rhythm.STRAIGHT
        self.structure = []
        
    def generate(self, structure_n=None):
        STRUCTURES_COUNT = 4
        if structure_n is None:
            structure_n = random.randint(0, STRUCTURES_COUNT)
        if structure_n > STRUCTURES_COUNT:
            raise ValueError('Structure number cannot be greater than {}, value {} is given'.format(STRUCTURES_COUNT, structure_n))
        structure = []

        if structure_n == 0:
            intro = SongBlock('Intro', 2)
            verse = SongBlock('Verse', 16)
            pre_chorus = SongBlock('Pre-Chorus', 4)
            chorus = SongBlock('Chorus', 8)
            breakdown = SongBlock('Breakdown', 16)
            pre_breakdown = SongBlock('Break', 8)
            breakdown2 = SongBlock('Breakdown', 16)
            structure.append(intro.dump())
            structure.append(verse.dump())
            structure.append(pre_chorus.dump())
            structure.append(chorus.dump())
            structure.append(verse.dump())
            structure.append(breakdown.dump())
            structure.append(chorus.dump())
            structure.append(pre_breakdown.dump())
            structure.append(breakdown2.dump())
            structure.append(chorus.dump())
            structure.append(verse.dump())

        if structure_n == 1:
            intro = SongBlock('Intro', 2)
            verse = SongBlock('Verse', 16)
            verse2 = SongBlock('Verse', 16)
            chorus = SongBlock('Chorus', 8)
            bridge = SongBlock('Break', 4)
            structure.append(intro.dump())
            structure.append(chorus.dump())
            structure.append(verse.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(verse.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(bridge.dump())
            structure.append(chorus.dump())
            structure.append(chorus.dump())

        if structure_n == 2:
            intro = SongBlock('Intro')
            verse = SongBlock('Verse')
            verse2 = SongBlock('Verse')
            chorus = SongBlock('Chorus')
            intro_modified = SongBlock('Intro')
            bridge = SongBlock('Break')
            solo = SongBlock('Verse')
            structure.append(intro.dump())
            structure.append(verse.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(verse.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(intro_modified.dump())
            structure.append(solo.dump())
            structure.append(chorus.dump())
            structure.append(verse2.dump())

        if structure_n == 3:
            verse = SongBlock('Verse')
            verse2 = SongBlock('Verse')
            chorus = SongBlock('Chorus')
            pre_breakdown = SongBlock('Breakdown')
            breakdown = SongBlock('Breakdown')
            structure.append(verse.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(pre_breakdown.dump())
            structure.append(breakdown.dump())
            structure.append(verse2.dump())
            structure.append(chorus.dump())
            structure.append(breakdown2.dump())
            structure.append(breakdown2.dump())
            structure.append(chorus.dump())
            structure.append(breakdown2.dump())

        if structure_n == 4:
            breakdown = SongBlock('Breakdown')
            breakdown2 = SongBlock('Breakdown')
            breakdown3 = SongBlock('Breakdown')
            pre_breakdown = SongBlock('Breakdown')
            verse = SongBlock('Verse')
            structure.append(breakdown.dump())
            structure.append(verse.dump())
            structure.append(breakdown2.dump())
            structure.append(verse.dump())
            structure.append(breakdown.dump())
            structure.append(pre_breakdown.dump())
            structure.append(breakdown3.dump())
            structure.append(breakdown3.dump())

        self.structure = structure
        return structure

    def dump(self):
        return self.structure

if __name__ == '__main__':
    structure = SongStructureClass()