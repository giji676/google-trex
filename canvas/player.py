from .constants import GROUND_HEIGHT, WIDTH, HEIGHT
import pygame


class Player:
    def __init__(self):
        self.jumping = False
        self.jump_count = 10
        self.x1 = 50
        self.y1 = 75
        self.x2 = 100
        self.y2 = 150
        self.actual_height = GROUND_HEIGHT - (self.y1 * 2)
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hitbox = (self.x1, self.actual_height, self.x2, self.y2)
        self.player_art = pygame.image.load("player.png")

    def jump_true(self):
        self.jumping = True

    def jump(self):
        self.neg = 1
        if self.jump_count < 0:
            self.neg = -1
        self.actual_height -= ((self.jump_count ** 2) * 0.5 * self.neg)/0.9
        self.hitbox = (self.x1, self.actual_height, self.x2, self.y2)
        self.jump_count -= 1

    def draw_player(self):
        self.gameDisplay.blit(self.player_art, (self.hitbox[0], self.hitbox[1]))
