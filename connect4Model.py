#import sys
#import numpy as np

from connect4GlobalConstants import *

class Connect4Model:
    def __init__(self):
        self.game_over = False
        self.current_player = 0

        #self.board = np.zeros((ROW_COUNT,COLUMN_COUNT))

        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def print_board(self):
        out =""
        for c in range(COLUMN_COUNT):
            row_string=""
            for r in range(ROW_COUNT):
                row_string +=str(self.board[r][c])
            out += row_string + "\n"
        print(out)

    # Fills the board with the location the player selected with corresponding disk.
    def drop_disk(self,disk_column, disk):
        #self.board
        disk_row = self.get_next_open_row(disk_column)
        self.board[disk_row][disk_column] = disk

    # Checks that the top row of the selected column is empty.
    def is_valid_column(self, disk_column):
        #self.board
        return self.board[ROW_COUNT - 1][disk_column] == 0

    # Finds the first empty row in a column where a disk is dropped.
    def get_next_open_row(self, disk_column):
        #self.board
        for r in range(ROW_COUNT):
            if self.board[r][disk_column] == 0:
                return r

    # Check if the last move is a winning move.
    def winning_move(self, disk):
        #self.board
        # Check horizontal
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (self.board[r][c] == disk and
                        self.board[r][c + 1] == disk and
                        self.board[r][c + 2] == disk and
                        self.board[r][c + 3] == disk):
                    return True

        # Check vertical
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (self.board[r][c] == disk and
                        self.board[r + 1][c] == disk and
                        self.board[r + 2][c] == disk and
                        self.board[r + 3][c] == disk):
                    return True

        # Check upwards diagonal
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (self.board[r][c] == disk and
                        self.board[r + 1][c + 1] == disk and
                        self.board[r + 2][c + 2] == disk and
                        self.board[r + 3][c + 3] == disk):
                    return True

        # Check downwards diagonal
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (self.board[r][c] == disk and
                        self.board[r - 1][c + 1] == disk and
                        self.board[r - 2][c + 2] == disk and
                        self.board[r - 3][c + 3] == disk):
                    return True