import pygame
from utils.setup import *

class button():
    def __init__(self, xPos, yPos, width=80, height=30):
        self.width = width
        self.height = height
        self.xPos = xPos
        self.yPos = yPos
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.colour = (0, 0, 0)
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def draw(self, btnText):
        textSurface = self.font.render(btnText, True, self.colour)
        x = (self.width-textSurface.get_rect().width) / 2 + self.xPos
        y = (self.height-textSurface.get_rect().height)/2 + self.yPos
        WIN.blit(textSurface, (x, y))

        pygame.draw.rect(WIN, self.colour, (self.xPos, self.yPos,
                                                 self.width, self.height), 2)

    def checkIfClicked(self, mPos):
        if self.rect.collidepoint(mPos):
            return True


class submitButton(button):
    def __init__(self):
        self.width = BUTTONWIDTH
        self.height = BUTTONHEIGHT
        super().__init__(xPos=WIDTH/2 - self.width*1.3,
                         yPos=(HEIGHT - SQUARESIZE*10)/2 + SQUARESIZE*10)

    def draw(self):
        super().draw('Solve')


class clearButton(button):
    def __init__(self):
        self.width = BUTTONWIDTH
        self.height = BUTTONHEIGHT
        super().__init__(WIDTH/2 + self.width * 0.3,
                         (HEIGHT - SQUARESIZE*10)/2 + SQUARESIZE*10)

    def draw(self):
        super().draw('Clear')
