import pygame
import math
import random

class Explosao(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/explosion00.png"))
        self.sprites.append(pygame.image.load("data/explosion01.png"))
        self.sprites.append(pygame.image.load("data/explosion02.png"))
        self.sprites.append(pygame.image.load("data/explosion03.png"))
        self.sprites.append(pygame.image.load("data/explosion04.png"))
        self.sprites.append(pygame.image.load("data/explosion05.png"))
        self.sprites.append(pygame.image.load("data/explosion06.png"))
        self.sprites.append(pygame.image.load("data/explosion07.png"))
        self.sprites.append(pygame.image.load("data/explosion08.png"))


        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = self.image.get_rect()

    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

