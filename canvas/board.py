from .constants import WIDTH, HEIGHT, GREY, WHITE, GROUND_HEIGHT
import pygame


class Board:
    def __init__(self):
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.ground = pygame.image.load("ground.png")
        self.ground_x = 0

    def draw_ground(self, win):
        win.fill(WHITE)
        pygame.draw.rect(win, GREY, (0, GROUND_HEIGHT, WIDTH, 3))

    def draw_ground_dots(self):
        if self.ground_x <= -2000:
            self.ground_x = 0
        self.gameDisplay.blit(self.ground, (self.ground_x, GROUND_HEIGHT + 3))
        self.gameDisplay.blit(self.ground, (self.ground_x + 2000, GROUND_HEIGHT + 3))
