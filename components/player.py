import pygame
from os import path
from utils.constants import (
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR,
    POWERUP_TIME
)
from components.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "alien.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        self.movement_on_x = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.centerx += 5

        if key[pygame.K_LEFT]:
            if self.rect.left < SCREEN_WIDTH and self.rect.left > 0:
                self.rect.centerx -= 5

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()


    def shoot(self):
        if self.power == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.bullets.add(bullet)
        if self.power >= 2:
            bullet1 = Bullet(self.rect.right, self.rect.centery)
            bullet2 = Bullet(self.rect.left, self.rect.centery)
            self.game.all_sprites.add(bullet1)
            self.game.all_sprites.add(bullet2)
            self.bullets.add(bullet1)
            self.bullets.add(bullet2)