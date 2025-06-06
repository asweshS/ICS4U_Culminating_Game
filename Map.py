import pygame # INSTALL PYGAME BY DOING "pip install pygame" in terminal
import sys

# Map settings
GRID_WIDTH = 15 # Width of the grid
GRID_HEIGHT = 10 # Height of the grid
CELL_SIZE = 65 # Size of the cells
MARGIN = 2 # Space between cells

# Colors
BG_COLOR = (30, 30, 30) # Black -- PLACEHOLDER
GRID_COLOR = (200, 200, 200) # White  -- PLACEHOLDER

# Function to draw the grid map
# This function draws a grid map with specified width and height, cell size, and margin.
def draw_map(screen):
    for row in range(GRID_HEIGHT):
        for color in range(GRID_WIDTH):
            rect = pygame.Rect(color * (CELL_SIZE + MARGIN) + MARGIN, row * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 2)

def main():
    # initialize Pygame and create the main window
    pygame.init()
    screen_width = GRID_WIDTH * (CELL_SIZE + MARGIN) + MARGIN
    screen_height = GRID_HEIGHT * (CELL_SIZE + MARGIN) + MARGIN
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Conquest: A Territory Strategy Game!")

    running = True
    # Main loop to keep the window open and handle events
    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with the background color and draw the grid map
        screen.fill(BG_COLOR)
        draw_map(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
