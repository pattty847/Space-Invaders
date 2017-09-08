import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage all bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.check_gun_state = False

        #Create a bullet rect at (0, 0) and then set correct position.
        # self.rect = pygame.Rect(0, 0, ai_settings.norm_bullet_width, ai_settings.norm_bullet_height)
        self.rect = pygame.Rect(0, 0, ai_settings.missel_width, ai_settings.missel_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.norm_bullet_color
        self.speed_factor = ai_settings.norm_bullet_speed


    def update(self):
        """Move the bullet up the screen"""
        #Update decimal value of bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)