import pygame
import setup


class square():
    def __init__(self, x=0, y=0):
        self.number = ''
        self.width = setup.SQUARESIZE
        self.height = setup.SQUARESIZE
        self.defFont = pygame.font.SysFont('Comic Sans MS', 20)
        self.filledFont = pygame.font.SysFont('Comic Sans MS', 20)

        self.defColour = (0, 0, 0)
        self.selectedColour = (255, 0, 0)
        self.xPos = x
        self.yPos = y
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.coord = [-1, -1]

        self.selected = False
        self.filled = False

    def getRect(self):
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        return self.rect

    def draw(self):
        squareColour = self.selectedColour if self.selected else self.defColour
        squareFont = self.defFont if not self.filled else self.filledFont
        squareThickness = 5 if self.filled else 2

        # Draw bounding rectangle
        pygame.draw.rect(setup.WIN, squareColour, (self.xPos,
                                                   self.yPos, self.width, self.height), squareThickness)

        textSurface = squareFont.render(self.number, True, squareColour)
        x = (self.width-textSurface.get_rect().width) / 2 + self.xPos
        y = self.height/2-textSurface.get_rect().height + self.yPos
        setup.WIN.blit(textSurface, (x, y))


class miniGrid():
    def __init__(self, xPos=0, yPos=0):
        self.size = 3 * setup.SQUARESIZE
        self.colour = (0, 0, 0)
        self.xPos = xPos
        self.yPos = yPos

    def draw(self):
        pygame.draw.rect(setup.WIN, self.colour, (self.xPos,
                                                  self.yPos, self.size, self.size), 4)
