import classes.utils as utils

class Note():

    def __init__(self, note_value, pitch=None, volume=None):

        if pitch is not None and type(pitch) is str:
            pitch = utils.get_pitch_from_str(pitch)

        if note_value is not None and type(note_value) is str:
            note_value = utils.get_note_value_from_str(note_value)

        if pitch is None:
            self._midi_data_block = (0, note_value, 0)
        else:
            self._midi_data_block = (pitch, note_value, volume)

    @property
    def pitch(self):
        return self._midi_data_block[0]

    @pitch.setter
    def pitch(self, new_pitch):
        if type(new_pitch) is str:
            new_pitch = utils.get_pitch_from_str(new_pitch)
        self._midi_data_block[0] = int(new_pitch)

    @property
    def volume(self):
        return self._midi_data_block[2]

    @volume.setter
    def volume(self, new_volume):
        self._midi_data_block[2] = int(new_volume)

    @property
    def value(self):
        return self._midi_data_block[1]

    @value.setter
    def value(self, new_value):
        if type(new_value) is str:
            new_value = utils.get_note_value_from_str(new_value)
        self._midi_data_block[1] = int(new_value)

    @property
    def is_pause(self):
        return (self.pitch == 0)