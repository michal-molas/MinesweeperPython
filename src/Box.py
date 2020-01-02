import pygame


class Box:
    uncov_textures = [pygame.image.load("../assets/none.png"), pygame.image.load("../assets/one.png"),
                      pygame.image.load("../assets/two.png"), pygame.image.load("../assets/three.png"),
                      pygame.image.load("../assets/four.png"), pygame.image.load("../assets/five.png"),
                      pygame.image.load("../assets/six.png"), pygame.image.load("../assets/seven.png"),
                      pygame.image.load("../assets/eight.png"), pygame.image.load("../assets/bomb.png"),]

    cov_textures = [pygame.image.load("../assets/empty.png"),
                    pygame.image.load("../assets/flag.png"),
                    pygame.image.load("../assets/question_mark.png")]

    val_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "bomb": 9,
    }

    state_dict = {
        "empty": 0,
        "flag": 1,
        "question_mark": 2
    }

    def __init__(self):
        self.value = "0"
        self.state = "empty"

        self.uncovered = False

    def change_state(self, st):
        if not self.uncovered:
            self.state = st

    def change_value(self, val):
        self.value = val
