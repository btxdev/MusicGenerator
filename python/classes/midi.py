from midiutil.MidiFile import MIDIFile
from pathlib import Path

class CreateMidiFile(object):

    def __init__(self, name='untitled', tempo=120):
        self._name = name
        self._mf = MIDIFile(1)
        self._mf.addTrackName(0, 0, name)
        self._mf.addTempo(0, 0, tempo)

    def add_note(self, channel, note, time):
        volume = int(note.volume * 127)
        self._mf.addNote(0, channel, note.pitch, time * 2, note.value, volume)

    def save(self, path):
        path = str(Path(path, self._name + '.mid').resolve())
        with open(path, 'wb') as file:
            self._mf.writeFile(file)
            print('file {} saved'.format(path))