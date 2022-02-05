import pygame

pygame.init()
pygame.display.set_caption('Sudoku solver')

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

SQUARESIZE = 50
BUTTONWIDTH = 80
BUTTONHEIGHT = 30