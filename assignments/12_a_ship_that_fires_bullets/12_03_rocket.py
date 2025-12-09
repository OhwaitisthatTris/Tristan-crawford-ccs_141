import pygame
import sys

class Rocket:
    def __init__(self, screen):
        # Load rocket image (use your own rocket.bmp or rocket.png)
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket in the center of the screen
        self.rect.center = self.screen_rect.center

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        # Move rocket but keep it inside screen boundaries
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 5
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 5
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocket Game")

    rocket = Rocket(screen)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = True

            # Key released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False

        # Update rocket position
        rocket.update()

        # Draw everything
        screen.fill