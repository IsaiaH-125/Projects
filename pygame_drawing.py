# Pygame_Drawing
# Author: isaiah
# Date: Nov 9/21

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main() -> None:
    """Driver of the python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("WINDOW_TITLE")



    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()


    # ---------------- Main loop
    while not done:
    # Create the main loop
        # --------------- listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ------------ environment
        # ------------ DRAW THE ENVIRONMENT
        screen.fill(WHITE)          #fill with bgcolor
        pygame.draw.rect(screen, RED, [100, 100, 75, 30])

        pygame.draw.circle(screen, BLACK, (500, 200), 60)
        pygame.draw.circle(screen, BLACK, (700, 200), 60)
        pygame.draw.circle(screen, GREY, (500, 200), 55)
        pygame.draw.circle(screen, GREY, (700, 200), 55)
        pygame.draw.circle(screen, BLACK, (600, 255), 75)
        pygame.draw.circle(screen, GREY, (600, 255), 65)
        pygame.draw.circle(screen, WHITE, (580, 200), 10)

        # Update the screen
        pygame.display.flip()
        # Tick the clock
        clock.tick(60)
if __name__ == '__main__':
    main()

