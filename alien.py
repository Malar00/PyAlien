import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('/run/media/malar/Data/Github/PyAlien/assets/Spaceship_02_RED.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
