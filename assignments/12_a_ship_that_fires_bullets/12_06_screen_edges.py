import pygame
import sys

# --- Ship Class ---
class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.bmp")  # Use your own ship image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 5

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 3)  # Small rectangle bullet
        self.rect.midleft = ship.rect.midright
        self.color = (255, 0, 0)  # Red bullet
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)