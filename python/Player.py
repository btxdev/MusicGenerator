from scamp import *

class PlayerClass(object):

    def __init__(self, tempo=None):
        if tempo is None:
            tempo = 120
        self.session = Session(tempo=tempo)
        self.channels = {}
    
    def ch_id(self, channel):
        return channel + 1

    def create_channel(self, name):
        channel = self.session.new_midi_part(name, self.ch_id(len(self.channels)))
        self.channels[name] = channel

    def _play_song_f(self, tabs, channel_name):
        channel = self.channels[channel_name]
        for notes in tabs:
            if len(notes) > 1:
                # chord
                pitches = []
                volumes = []
                values = []
                for note in notes:
                    pitches.append(note.pitch)
                    volumes.append(note.volume)
                    values.append(note.value)
                    volume = max(volumes)
                    value = max(values)
                channel.play_chord(pitches, volume, value)
            else:
                # single note
                note = notes[0]
                if note.pitch == 0:
                    wait(note.value)
                else:
                    channel.play_note(note.pitch, note.volume, note.value)
        
    def play(self, tabs, channel_name):
        self.session.fork(self._play_song_f(tabs, channel_name))

    def sync(self):
        self.session.wait_for_children_to_finish()