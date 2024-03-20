class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


SIZE = 8


# noinspection PyMethodMayBeStatic
class Checkers:
    col_index = 'ABCDEFGH'

    def __init__(self):
        self.cells = self.create_cells()

    def create_cells(self):
        board = []
        for i in range(SIZE):
            board.append([])
            for j in range(SIZE):
                if (i + j) % 2 and i < 3:
                    board[i].append(Cell('B'))
                elif (i + j) % 2 and i > 4:
                    board[i].append(Cell('W'))
                else:
                    board[i].append(Cell('X'))

        return board[::-1]

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

