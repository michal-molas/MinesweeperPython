import pygame
import random
from src.Box import *


class Game:
    def __init__(self, width, height, num_bombs):
        self.w = width
        self.h = height
        self.num_b = num_bombs
        self.board = []

        self.finished = False

        for i in range(height):
            board_row = []
            for j in range(width):
                board_row.append(Box())
            self.board.append(board_row)

    def generate_board(self, y, x):
        # generating bombs

        bombs = []
        while len(bombs) < self.num_b:
            rand_x = random.randrange(self.w)
            rand_y = random.randrange(self.h)
            if ((rand_x, rand_y) not in bombs) and ((rand_x, rand_y) != (x, y)):
                bombs.append((rand_x, rand_y))

        for b in bombs:
            self.board[b[1]][b[0]].change_value("bomb")

        # counting bombs

        for i in range(self.h):
            for j in range(self.w):
                cnt = 0
                if self.board[i][j].value != "bomb":
                    if i > 0:
                        if self.board[i - 1][j].value == "bomb":
                            cnt += 1
                        if j > 0:
                            if self.board[i - 1][j - 1].value == "bomb":
                                cnt += 1
                        if j < self.w - 1:
                            if self.board[i - 1][j + 1].value == "bomb":
                                cnt += 1
                    if i < self.h - 1:
                        if self.board[i + 1][j].value == "bomb":
                            cnt += 1
                        if j > 0:
                            if self.board[i + 1][j - 1].value == "bomb":
                                cnt += 1
                        if j < self.w - 1:
                            if self.board[i + 1][j + 1].value == "bomb":
                                cnt += 1
                    if j > 0:
                        if self.board[i][j - 1].value == "bomb":
                            cnt += 1
                    if j < self.w - 1:
                        if self.board[i][j + 1].value == "bomb":
                            cnt += 1
                    
                    self.board[i][j].change_value(str(cnt))

    def draw(self, win):
        win.fill((255, 255, 255))
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j].uncovered:
                    win.blit(Box.uncov_textures[Box.val_dict[self.board[i][j].value]], (32 * j, 32 * i))
                else:
                    win.blit(Box.cov_textures[Box.state_dict[self.board[i][j].state]], (32 * j, 32 * i))
        pygame.display.update()
