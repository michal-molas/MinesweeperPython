import pygame
import os


class Box:
    current_path = os.path.dirname(__file__)
    assets_path = os.path.join(current_path, "assets")
    textures = [pygame.image.load("../assets/empty.png"), pygame.image.load("../assets/one.png"),
                pygame.image.load("../assets/two.png"), pygame.image.load("../assets/three.png"),
                pygame.image.load("../assets/four.png"), pygame.image.load("../assets/five.png"),
                pygame.image.load("../assets/six.png"), pygame.image.load("../assets/seven.png"),
                pygame.image.load("../assets/eight.png"), pygame.image.load("../assets/none.png"),
                pygame.image.load("../assets/bomb.png"), pygame.image.load("../assets/flag.png"),
                pygame.image.load("../assets/question_mark.png")]

    val_dict = {
        "empty": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "0": 9,
        "bomb": 10,
        "flag": 11,
        "question_mark": 12
    }

    def __init__(self):
        self.value = "empty"
        self.tex = Box.textures[0]

    def change_value(self, val):
        self.value = val
        self.tex = Box.textures[Box.val_dict[val]]
