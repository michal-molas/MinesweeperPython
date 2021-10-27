import sys
import pygame
from src.Game import *
from src.Player import *


def run(width, height, num_bombs):
    pygame.init()
    game = Game(width, height, num_bombs)
    player = Player()
    win = pygame.display.set_mode((width * 32, height * 32))

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
    if len(sys.argv) > 4:
        print('Too many arguments.')
    elif len(sys.argv) < 4:
        print('Not enough arguments.')
    else:
        correct_input = True
        for i in range(1, 4):
            if not sys.argv[i].isdigit() or int(sys.argv[i]) < 0:
                print('Argument ' + sys.argv[i] + ' is not a positive integer.')
                correct_input = False

        if correct_input:
            width = int(sys.argv[1])
            height = int(sys.argv[2])
            num_bombs = int(sys.argv[3])

            if width > 50 or width <= 0:
                print('Width must be in range from 1 to 50.')
                correct_input = False
            if height > 25 or height <= 0:
                print('Height must be in range from 1 to 25.')
                correct_input = False
            if num_bombs <= 0 or num_bombs > width * height - 1:
                print('number of bombs must be in range from 1 to (width * height - 1)')
                correct_input = False
            
            if correct_input:
                run(width, height, num_bombs)
