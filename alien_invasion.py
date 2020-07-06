import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # background = pygame.Surface((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(game_settings, screen)
    gf.create_fleet(game_settings, screen, aliens)


    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        gf.check_events(ship, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)
        pygame.display.flip()


run_game()
