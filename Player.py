import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        x_player = 50
        y_player = 50
        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(x_player, y_player, 100, 100)
        self.speed = 0
        self.acceleration = 0.2

    def update(self, *args):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_s]:
            self.speed += self.acceleration
        elif keys[pygame.K_w]:
            self.speed -= self.acceleration
        else:
            self.speed *= 0.95

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = -self.speed
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = -self.speed