class Grid:
    def __init__(self, grid):
        self.max_len = 5
        self.grid = grid
        self.win_board = [[False for _ in range(self.max_len)] for _ in range(self.max_len)]

    def is_winner(self):
        """Return True if the grid(2D) wins by checking the rows and the cols"""

        # checking the rows of the win_board
        for row in self.win_board:
            if len(set(row)) == 1 and list(set(row))[0]:
                # we have a winning board
                return True

        # checking the cols
        for i in range(self.max_len):
            if self.win_board[0][i] and self.win_board[1][i] and self.win_board[2][i] and self.win_board[3][i] and self.win_board[4][i]:
                return True

        return False

    def update_grid(self, inp):
        """ If inp value is found in the grid update its place in the win_board with True, then check the if it wins"""
        for i in range(self.max_len):
            for j in range(self.max_len):
                if self.grid[i][j] == inp:
                    self.win_board[i][j] = True

        return self.is_winner()

    def answer(self, ind):
        """Returns the answer by summing the values in the grid not visited * ind"""

        total = 0
        for i in range(self.max_len):
            for j in range(self.max_len):
                if not self.win_board[i][j]:
                    total += self.grid[i][j]

        return total * ind

with open('input.txt', 'r') as file_:
    records = file_.read().splitlines() 

    # removing the spaces 
    records = [record for record in records if record]
    grid_input = map(int, records.pop(0).split(','))

    # converting to 2D
    boards = [records[i:i+5] for i in range(0, len(records), 5)]

    formated_boards = []
    for grid in boards:
        grid_= []
        for sub_grid in grid:
            grid_.append(list(map(int, filter(None,sub_grid.split(' ')))))
        formated_boards.append(Grid(grid_))

    # game ends with the first win
    for inp in grid_input:
        for grid in formated_boards:
            if not grid.is_winner():
                # update the grid
                wins = grid.update_grid(inp)
                if wins:
                    print(grid.answer(inp))

