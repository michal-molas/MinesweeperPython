import pygame


class Player:

    def __init__(self):
        self.first_uncover = True

    def update(self, events, game):
        self.handle_events(events, game)
        self.check_board(game)

    def handle_events(self, events, game):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not game.finished:
                        mouse_pos = pygame.mouse.get_pos()
                        i = mouse_pos[1] // 32
                        j = mouse_pos[0] // 32
                        self.uncover_box(game, i, j)
                if event.button == 3:
                    if not game.finished:
                        mouse_pos = pygame.mouse.get_pos()
                        i = mouse_pos[1] // 32
                        j = mouse_pos[0] // 32
                        self.change_box_state(game, i, j)

    def check_board(self, game):
        if not self.first_uncover and not game.finished:
            cnt = 0
            for i in range(game.h):
                for j in range(game.w):
                    if game.board[i][j].state == "flag" and game.board[i][j].value == "bomb":
                        cnt += 1
            if cnt == game.num_b:
                game.finished = True
                print("Congratulations, you won!!!")

    def change_box_state(self, game, i, j):
        curr_st = game.board[i][j].state
        if curr_st == "empty":
            game.board[i][j].change_state("flag")
        elif curr_st == "flag":
            game.board[i][j].change_state("question_mark")
        else:
            game.board[i][j].change_state("empty")

    def uncover_box(self, game, i, j):
        if self.first_uncover:
            self.first_uncover = False
            game.generate_board(i, j)
        if not game.board[i][j].uncovered and game.board[i][j].state == "empty":
            game.board[i][j].uncovered = True
            if game.board[i][j].value == "bomb":
                game.finished = True
                print("GAME OVER!!!!!!")
            if game.board[i][j].value == "0":
                self.uncover_surrounding(game, i, j)

    def uncover_surrounding(self, game, i, j):
        if i > 0:
            self.uncover_box(game, i - 1, j)
            if j > 0:
                self.uncover_box(game, i - 1, j - 1)
            if j < game.w - 1:
                self.uncover_box(game, i - 1, j + 1)
        if i < game.h - 1:
            self.uncover_box(game, i + 1, j)
            if j > 0:
                self.uncover_box(game, i + 1, j - 1)
            if j < game.w - 1:
                self.uncover_box(game, i + 1, j + 1)
        if j > 0:
            self.uncover_box(game, i, j - 1)
        if j < game.w - 1:
            self.uncover_box(game, i, j + 1)
