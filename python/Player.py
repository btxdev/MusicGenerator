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

    # def channel(self, name):
    #     return self.channels[name]

    def _play_song_f(self, song, channel_name):
        for note in song:
            pitch = note[0]
            duration = note[1]
            volume = note[2]
            if pitch == 0:
                wait(duration)
            else:
                channel = self.channels[channel_name]
                channel.play_note(pitch, volume, duration)
        
    def play(self, song, channel_name):
        self.session.fork(self._play_song_f(song, channel_name))
        self.session.wait_for_children_to_finish()