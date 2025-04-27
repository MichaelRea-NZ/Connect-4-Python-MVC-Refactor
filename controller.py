from connect4Model import Connect4Model
from connect4PygameView import Connect4PygameView

class GameController:
    if __name__ == '__main__':
        #initialize_view()
        #initialize_model()
        model = Connect4Model()
        model.print_board()

        view = Connect4PygameView(model)
        view.go()


        """ the main game loop. It runs so long as game_over is false. for
         game_over to become true a player must get 4 of their disks in a line."""
        # while not game_over:
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #
        #         if event.type == get_mouse_motion():
        #             pygame.draw.rect(screen, BACKGROUND,
        #                              (0, 0, WIDTH, GAP_SIZE))
        #             x = event.pos[0]
        #             if current_player == 0:
        #                 draw_disk(PLAYER_1, x)
        #             else:
        #                 draw_disk(PLAYER_2, x)
        #
        #             update_board()
        #
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             pygame.draw.rect(screen, BACKGROUND,
        #                              (0, 0, WIDTH, GAP_SIZE))
        #             if current_player == 0:
        #                 x = event.pos[0]
        #                 column = int(math.floor(x / GAP_SIZE))
        #
        #                 if is_valid_column(column):
        #                     # row = get_next_open_row(column)
        #                     drop_disK(column, 1)
        #
        #                     if winning_move(1):
        #                         player_1_wins()
        #                         game_over = True
        #
        #             else:
        #                 x = event.pos[0]
        #                 column = int(math.floor(x / GAP_SIZE))
        #
        #                 if is_valid_column(column):
        #                     # row = get_next_open_row(column)
        #                     drop_disk(column, 2)
        #
        #                     if winning_move(2):
        #                         player_2_wins()
        #                         game_over = True
        #
        #             draw_board()
        #
        #             # need to comment about how ^ work
        #             current_player = current_player ^ 1
        #             if game_over:
        #                 pygame.time.wait(3000)