class Game:
    def __init__(self, game_input, size):
        self.board = game_input
        self.size = size

    # given a board, return a new board with the next step
    def new_step(self):
        new_board = []
        for i in range(self.size):
            new_line = []
            for j in range(self.size):
                new_cell = '0'
                if self.cell_continues_alive(i, j): new_cell = '1'
                new_line.append(new_cell)
            new_board.append(new_line)
            
        return new_board

    # given a cell, return if it continues alive or not
    def cell_continues_alive(self, line, collumn):
        nearby_cells_alive = self.check_neighborhood(line, collumn)
        cell = self.board[line][collumn]
        new_cell = False

        if cell == '1':
            if nearby_cells_alive < 2 or nearby_cells_alive > 3: new_cell = False
            else: new_cell = True
        else:
            if nearby_cells_alive == 3: new_cell = True

        return new_cell

    # given a cell, return the number of nearby cells alive
    def check_neighborhood(self, line, collumn):
        nearby_cells_alive = 0
        size = self.size
        for i in range(line-1, line+2):
            for j in range(collumn-1, collumn+2):
                if (i>=0 and j>=0) and (i<size and j<size):
                    if not (i==line and j==collumn):
                        if self.board[i][j] == '1': nearby_cells_alive += 1
        
        return nearby_cells_alive

    # given a board, print it
    def show(self, new_board):
        for i in range(len(new_board)):
            print(''.join(new_board[i]))


if __name__ == '__main__':
    lines = int(input())
    game_input = []
    for i in range(lines):
        line = list(input())
        game_input.append(line)

    new_game = Game(game_input, lines)
    new_new_step = new_game.new_step()
    new_game.show(new_new_step)