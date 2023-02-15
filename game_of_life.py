class Game:
    def __init__(self, game_input, size):
        self.board = game_input
        self.size = size

    # return a new board with the next step
    def new_step(self):
        new_board = []
        for i in range(self.size):
            new_line = []
            for j in range(self.size):
                new_cell = '0'
                if self.cell_continues_alive(i, j): new_cell = '1'
                new_line.append(new_cell)
            new_board.append(new_line)
            
        self.board = new_board
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

    # return the board
    def get_board(self):
        return self.board

    # return if the game is over or not
    def check_game_over(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == '1': return False
        return True

    # print the board
    def show_board(self):
        for i in range(len(self.board)):
            print(''.join(self.board[i]))


if __name__ == '__main__':
    lines = int(input())
    game_input = []
    for i in range(lines):
        line = list(input())
        game_input.append(line)

    game = Game(game_input, lines)
    game.new_step()
    game.show_board()

