import pygame
import random
from os import path
from utils.constants import (
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    BLACK,
    IMG_DIR
)
class Power_up(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'gun'
        self.image = pygame.image.load(path.join(IMG_DIR, "bullet.png"))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
