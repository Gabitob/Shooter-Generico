import pygame
import math
import random

class Inimigos(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/enemyShip.png")
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 1 + random.random() * 2

        self.time = None

    def update(self, *args):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
