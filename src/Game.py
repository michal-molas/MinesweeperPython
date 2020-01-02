import pygame
from src.Box import *


class Game:
    def __init__(self, width, height, num_bombs):
        self.w = width
        self.h = height
        self.board = []
        for i in range(height):
            board_row = []
            for j in range(width):
                board_row.append(Box())
            self.board.append(board_row)
        self.generate_board(num_bombs)

    def generate_board(self, num_bombs):
        pass

    def draw(self, win):
        win.fill((255, 255, 255))
        for i in range(self.h):
            for j in range(self.w):
                print(32 * j, 32 * i)
                win.blit(self.board[i][j].tex, (32 * j, 32 * i))
        pygame.display.update()
