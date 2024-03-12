class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    cells = ['XBXBXBXB',
             'BXBXBXBX',
             'XBXBXBXB',
             'XXXXXXXX',
             'XXXXXXXX',
             'WXWXWXWX',
             'XWXWXWXW',
             'WXWXWXWX'][::-1]

    col_index = 'ABCDEFGH'

    def __init__(self):
        self.cells = [[Cell(cell) for cell in row] for row in Checkers.cells]

    def get_cell(self, position):
        letter, digit = position
        i = Checkers.col_index.index(letter)
        j = int(digit) - 1
        return self.cells[j][i]

    def set_cell(self, position, state):
        letter, digit = position
        i = Checkers.col_index.index(letter)
        j = int(digit) - 1
        self.cells[j][i] = Cell(state)

    def move(self, start_position, final_position):
        self.set_cell(final_position, self.get_cell(start_position).status())
        self.set_cell(start_position, 'X')
