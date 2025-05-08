import numpy as np
import pygame
import sys
import math

# Measurement constants
COLUMN_COUNT = 7
ROW_COUNT = 6
GAP_SIZE = 100
WIDTH = COLUMN_COUNT * GAP_SIZE
HEIGHT = (ROW_COUNT + 1) * GAP_SIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = int(GAP_SIZE / 2 - 5)
# Colour constants
BLUE = (0, 0, 255)
LIGHT_BLUE = (205, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BACKGROUND = LIGHT_BLUE
PLAYER_1 = RED
PLAYER_2 = YELLOW

# Globals
game_over = False
current_player = 0
pygame.init()
game_font = pygame.font.SysFont("verdana", 75)
screen = pygame.display.set_mode(SIZE)

# creates a matrix of 6 rows and 7 columns.
board = np.zeros((ROW_COUNT, COLUMN_COUNT))


###############################################################################


# Model
# Fills the board with the location the player selected with corresponding disk.
def drop_disc(disk_column, disk):
    global board
    disk_row = get_next_open_row(column)
    board[disk_row][disk_column] = disk


# Checks that the top row of the selected column is empty.
def is_valid_column(disk_column):
    global board
    return board[ROW_COUNT - 1][disk_column] == 0


# Finds the first empty row in a column where a disk is dropped.
def get_next_open_row(disk_column):
    global board
    for r in range(ROW_COUNT):
        if board[r][disk_column] == 0:
            return r


# Check if the last move is a winning move.
def winning_move(disk):
    global board
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (board[r][c] == disk and
                    board[r][c + 1] == disk and
                    board[r][c + 2] == disk and
                    board[r][c + 3] == disk):
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == disk and
                    board[r + 1][c] == disk and
                    board[r + 2][c] == disk and
                    board[r + 3][c] == disk):
                return True

    # Check upwards diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == disk and
                    board[r + 1][c + 1] == disk and
                    board[r + 2][c + 2] == disk and
                    board[r + 3][c + 3] == disk):
                return True

    # Check downwards diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (board[r][c] == disk and
                    board[r - 1][c + 1] == disk and
                    board[r - 2][c + 2] == disk and
                    board[r - 3][c + 3] == disk):
                return True


###############################################################################

# View

def draw_board():
    global board
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (
            # GAP_SIZE + GAP_SIZE. The + GAP_SIZE makes the BLUE
            # start 1 GAP_SIZE from the top of the screen.
            c * GAP_SIZE, r * GAP_SIZE + GAP_SIZE, GAP_SIZE, GAP_SIZE))
            pygame.draw.circle(screen, BACKGROUND, (
            int(c * GAP_SIZE + GAP_SIZE / 2),
            int(r * GAP_SIZE + GAP_SIZE + GAP_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, PLAYER_1, (
                int(c * GAP_SIZE + GAP_SIZE / 2),
                HEIGHT - int(r * GAP_SIZE + GAP_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, PLAYER_2, (
                int(c * GAP_SIZE + GAP_SIZE / 2),
                HEIGHT - int(r * GAP_SIZE + GAP_SIZE / 2)), RADIUS)

    update_window()


def update_window():
    pygame.display.update()


# def print_board():
#     global board
#     print(np.flip(board, 0))

def draw_disk(player, disk_x):
    global screen
    pygame.draw.circle(screen, player, (disk_x, int(GAP_SIZE / 2)), RADIUS)


def update_board():
    pygame.display.update()


def get_mouse_motion():
    return pygame.MOUSEMOTION


def set_font():
    global game_font
    # game_font = pygame.font.SysFont("verdana", 75)


def player_1_wins():
    label = game_font.render("Player 1 won!", 1, PLAYER_1)
    screen.blit(label, (100, 1))


def player_2_wins():
    label = game_font.render("Player 2 won!", 1, PLAYER_2)
    screen.blit(label, (100, 1))


def initialize_view():
    global game_font, screen, board
    # game_font = pygame.font.SysFont("verdana", 75)
    screen = pygame.display.set_mode(SIZE)

    # print_board()

    draw_board()


def initialize_model():
    global game_over, current_player
    game_over = False

    current_player = 0


#############################################################################

# Controller
if __name__ == '__main__':
    initialize_view()
    initialize_model()

    """ the main game loop. It runs so long as game_over is false. for
     game_over to become true a player must get 4 of their disks in a line."""
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == get_mouse_motion():
                pygame.draw.rect(screen, BACKGROUND,
                                 (0, 0, WIDTH, GAP_SIZE))
                x = event.pos[0]
                if current_player == 0:
                    draw_disk(PLAYER_1, x)
                else:
                    draw_disk(PLAYER_2, x)

                update_board()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BACKGROUND,
                                 (0, 0, WIDTH, GAP_SIZE))
                if current_player == 0:
                    x = event.pos[0]
                    column = int(math.floor(x / GAP_SIZE))

                    if is_valid_column(column):
                        # row = get_next_open_row(column)
                        drop_disc(column, 1)

                        if winning_move(1):
                            player_1_wins()
                            game_over = True

                else:
                    x = event.pos[0]
                    column = int(math.floor(x / GAP_SIZE))

                    if is_valid_column(column):
                        # row = get_next_open_row(column)
                        drop_disc(column, 2)

                        if winning_move(2):
                            player_2_wins()
                            game_over = True

                draw_board()

                # need to comment about how ^ work
                current_player = current_player ^ 1
                if game_over:
                    pygame.time.wait(3000)
