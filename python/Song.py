import Key
import Mood

class SongClass(object):
    def __init__(self):
        self.tempo = 120
        self.time_signature = 4
        self.structure_novelty = 0.5
        
        self.mood_agression = 0.5
        self.mood_sadness = 0.5
        self.mood_epic = 0.5

        self.base_key = Key.Random()
        self.melodic_complexity = 0.5
        self.melodic_novelty = 0.5

        self.chord_complexity = 0.5
        self.chord_novelty = 0.5

        self.chord_melody_tension = 0.5

        self.rhythm_novelty = 0.5
        self.danceability = 0.5

        self.acoustic_wideness = 0.5