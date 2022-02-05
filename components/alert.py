import pygame
from utils.setup import *

class alert():
    def __init__(self, WIDTH):
        self.width = 200
        self.height = 40
        self.xPos = WIDTH/2 - self.width/2
        self.yPos = 30
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.colour = (0, 0, 0)
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def draw(self, btnText):
        textSurface = self.font.render(btnText, True, self.colour)
        x = (self.width-textSurface.get_rect().width) / 2 + self.xPos
        y = (self.height-textSurface.get_rect().height)/2 + self.yPos

        pygame.draw.rect(WIN, (200, 200, 200), (self.xPos, self.yPos,
                                                self.width, self.height), 0)
        WIN.blit(textSurface, (x, y))