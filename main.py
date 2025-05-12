import pygame
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from src.globals import g

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
g.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.Surface.convert_alpha(g.window)
pygame.display.set_caption("Auto Arena")

from src.game import Game

game = Game()
while True:
    game.update()
    pygame.display.flip()
    fpsClock.tick(FPS)
