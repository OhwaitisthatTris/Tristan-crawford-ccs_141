import pygame
import sys

def run_game():
    # Initialize Pygame
    pygame.init()

    # Create an empty screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Event Demo")

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Detect key presses
            elif event.type == pygame.KEYDOWN:
                print(f"Key pressed: {event.key}")

        # Fill screen with black
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
