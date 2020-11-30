import pygame

from utils.constants import (
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT/2

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.centerx += 5
        if key[pygame.K_LEFT]:
            if self.rect.left < SCREEN_WIDTH and self.rect.left > 0:
                self.rect.centerx -= 5