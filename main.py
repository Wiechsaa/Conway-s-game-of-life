import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Settings
WIDTH, HEIGHT = 1920, 1080
SIZE = (WIDTH, HEIGHT)
FPS = 60

BLACK = (0, 0, 0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)

SCALER = 20
OFFSET = 1

pygame.init()
pygame.display.set_caption(' Conway game of life')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

board = Grid(WIDTH, HEIGHT, SCALER, OFFSET)
board.random_2d_array()

    
if __name__ == '__main__':
    run = True
    while run:
        clock.tick(FPS)
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        board.game(off_color=WHITE, on_color=BLUE, surface=screen)           
    
        pygame.display.update()