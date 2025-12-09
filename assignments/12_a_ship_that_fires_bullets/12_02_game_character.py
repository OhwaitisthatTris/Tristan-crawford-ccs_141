import pygame
import sys

class GameCharacter:
    def __init__(self, image_path, screen):

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
        self.rect.center = screen.get_rect().center

        self.bg_color = self.image.get_at((0, 0))

    def draw(self, screen):
        screen.fill(self.bg_color)

        screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Character Example")

    character = GameCharacter("character.bmp", screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        character.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    run_game()
