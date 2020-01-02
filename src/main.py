import pygame
from src.InputWindow import *
from src.Game import *


def run():
    pygame.init()
    game = Game(20, 20, 100)
    win = pygame.display.set_mode((640, 640))

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        game.draw(win)


if __name__ == "__main__":
    run()
