from .constants import GROUND_HEIGHT, HEIGHT, WIDTH
import random
import pygame


class Obstacles:
    def __init__(self):
        self.hitbox = (0, 0, 0, 0)
        self.obstacles = [pygame.image.load("pack0.png"), pygame.image.load("pack1.png"),
                          pygame.image.load("pack2.png"), pygame.image.load("pack3.png"),
                          pygame.image.load("pack4.png")]
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.random_obstacles = random.choice(self.obstacles)
        self.x = WIDTH

    def new_obstacle(self):
        self.random_obstacles = random.choice(self.obstacles)

    def chose_random_obstacle(self):
        if self.random_obstacles == self.obstacles[0]:
            self.hitbox = (self.x, GROUND_HEIGHT - 60, 40, 60)
            self.gameDisplay.blit(self.random_obstacles, (self.hitbox[0], self.hitbox[1]))

        if self.random_obstacles == self.obstacles[1]:
            self.hitbox = (self.x, GROUND_HEIGHT - 70, 50, 70)
            self.gameDisplay.blit(self.random_obstacles, (self.hitbox[0], self.hitbox[1]))

        if self.random_obstacles == self.obstacles[2]:
            self.hitbox = (self.x, GROUND_HEIGHT - 60, 60, 60)
            self.gameDisplay.blit(self.random_obstacles, (self.hitbox[0], self.hitbox[1]))

        if self.random_obstacles == self.obstacles[3]:
            self.hitbox = (self.x, GROUND_HEIGHT - 70, 70, 70)
            self.gameDisplay.blit(self.random_obstacles, (self.hitbox[0], self.hitbox[1]))

        if self.random_obstacles == self.obstacles[4]:
            self.hitbox = (self.x, GROUND_HEIGHT - 80, 50, 80)
            self.gameDisplay.blit(self.random_obstacles, (self.hitbox[0], self.hitbox[1]))
