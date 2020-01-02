import pygame
from src.InputWindow import *
from src.Game import *
from src.Player import *


def run():
    pygame.init()
    game = Game(20, 20, 10)
    player = Player()
    win = pygame.display.set_mode((640, 640))

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        player.update(events, game)
        game.draw(win)


if __name__ == "__main__":
    run()
