from classes.note import Note

class Tablature():

    def __init__(self, tacts=8, precision=16):
        self.tabs = []
        self.tacts = int(tacts)
        self.precision = int(precision)

        self._last_position = 0

        if precision % 2 != 0:
            raise ValueError('parameter precision must be a multiple of 2, got value {} instead'.format(precision))
        # precision - how many parts contains in one tact

        value = 4 / precision
        for _ in range(tacts):
            for _ in range(precision):
                self.tabs.append([Note(value, 0, 0)])
    
    def paste(self, note_object, position=None):
        if position is None:
            position = self._last_position
        self._last_position += 1

        # delete pause
        if note_object.is_pause or (len(self.tabs[position]) == 1 and self.tabs[position][0].is_pause):
            self.tabs[position].clear()
        # else:
        #     # delete pause
        #     if len(self.tabs[position]) == 1:

        # for i in range(0, len(self.tabs)):
        #     for j in range(0, len(self.tabs[i]), -1):
        #         if self.tabs[i][j].is_pause:
        #             self.tabs[i][j].remove

        self.tabs[position].append(note_object)

    def print(self):
        for notes in self.tabs:
            if len(notes) != 0:
                out_msg = '['
                for note in notes:
                    if note.is_pause:
                        out_msg += 'pause'
                    else:
                        out_msg += '({}, {}, {})'.format(note.pitch, note.value, note.volume)
                out_msg += ']'
                print(out_msg)
            else:
                print('[]')
            
