import sys
import math
import pygame
from connect4GlobalConstants import *


class Connect4PygameView:

    def __init__(self, model):
        self.model = model
        self.initialize_model()
        self.pygame = pygame
        self.pygame.init()
        self.game_font = pygame.font.SysFont("verdana", 75)
        self.screen = pygame.display.set_mode(SIZE)


    def draw_board(self):
        #self.board
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (
                    # GAP_SIZE + GAP_SIZE. The + GAP_SIZE makes the BLUE
                    # start 1 GAP_SIZE from the top of the screen.
                    c * GAP_SIZE, r * GAP_SIZE + GAP_SIZE, GAP_SIZE, GAP_SIZE))
                pygame.draw.circle(self.screen, BACKGROUND, (
                    int(c * GAP_SIZE + GAP_SIZE / 2),
                    int(r * GAP_SIZE + GAP_SIZE + GAP_SIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if self.model.board [r][c] == 1:
                    pygame.draw.circle(self.screen, PLAYER_1, (
                        int(c * GAP_SIZE + GAP_SIZE / 2),
                        HEIGHT - int(r * GAP_SIZE + GAP_SIZE / 2)), RADIUS)
                elif self.model.board [r][c] == 2:
                    pygame.draw.circle(self.screen, PLAYER_2, (
                        int(c * GAP_SIZE + GAP_SIZE / 2),
                        HEIGHT - int(r * GAP_SIZE + GAP_SIZE / 2)), RADIUS)

        self.update_window()
        self.top()

    def top(self):
        pygame.draw.rect(self.screen, BACKGROUND,
                         (0, 0, WIDTH, GAP_SIZE))

    def update_window(self):
        self.pygame.display.update()
        #self.top()

    # def print_board():
    #     global board
    #     print(np.flip(board, 0))

    def draw_disk(self, player, disk_x):
        #self.screen
        pygame.draw.circle(self.screen, player, (disk_x, int(GAP_SIZE / 2)),
                           RADIUS)

    def update_board(self):
        self.pygame.display.update()


    def get_mouse_motion(self):
        return self.pygame.MOUSEMOTION

    def set_font(self):
        #self.pygame.game_font
        self.game_font = pygame.font.SysFont("verdana", 75)

    def player_1_wins(self):
        label = self.game_font.render("Player 1 won!", 1, PLAYER_1)
        self.screen.blit(label, (100, 1))

    def player_2_wins(self):
        label = self.game_font.render("Player 2 won!", 1, PLAYER_2)
        self.screen.blit(label, (100, 1))

    def initialize_view(self):
        #self.game_font, self.screen, self.board
        #game_font = pygame.font.SysFont("verdana", 75)
        #screen = pygame.display.set_mode(SIZE)


        self.model.print_board()

        #self.draw_board()

    def initialize_model(self):
        self.model.game_over = False
        self.model.current_player = 0

    def go(self):
        while not self.model.game_over:
            self.draw_board()
            #self.top()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                if event.type == self.get_mouse_motion():
                    pygame.draw.rect(self.screen, BACKGROUND,
                                         (0, 0, WIDTH, GAP_SIZE))
                    x = event.pos[0]
                    if self.model.current_player == 0:
                        self.draw_disk(PLAYER_1, x)
                    else:
                        self.draw_disk(PLAYER_2, x)

                    self.update_board()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BACKGROUND,
                                     (0, 0, WIDTH, GAP_SIZE))
                    if self.model.current_player == 0:
                        x = event.pos[0]
                        column = int(math.floor(x / GAP_SIZE))

                        if self.model.is_valid_column(column):
                           # row = get_next_open_row(column)
                            self.model.drop_disk(column, 1)

                            if self.model.winning_move(1):
                                self.player_1_wins()
                                self.model.game_over = True

                    else:
                        x = event.pos[0]
                        column = int(math.floor(x / GAP_SIZE))

                        if self.model.is_valid_column(column):
                            # row = get_next_open_row(column)
                            self.model.drop_disk(column, 2)

                            if self.model.winning_move(2):
                                self.player_2_wins()
                                self.model.game_over = True

                    self.draw_board()


                    # need to comment about how ^ work
                    self.model.current_player = self.model.current_player ^ 1
                    if self.model.game_over:
                        self.pygame.time.wait(5000)
