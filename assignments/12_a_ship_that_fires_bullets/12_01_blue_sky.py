import pygame
def __ init __ (self)
""Initialize the game, create game resources."""
    pygame.init()
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("alien Invasion")
 
    def run_game(self):
    """ Start the main loop for the game."""
while true:
# Watch for keyboard and mouse events.
for event in pygame.event.get():
if event.type == pygame.QUIT:
    sys.exit()

    #make the most recenlty drawn screen visble
    pygame.display.flip()

    if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()