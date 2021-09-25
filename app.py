import pygame

from squares import square, miniGrid
from buttons import submitButton, clearButton
from board import board
from alert import alert

import setup

pygame.init()
pygame.display.set_caption('Sudoku solver')


class game():
    def __init__(self):
        self.board = board()
        self.submitBtn = submitButton()
        self.clearBtn = clearButton()
        self.selectedSqCoord = self.board.selectedSqCoord
        self.alert = alert()

    def render(self):
        self.board.drawBoard()
        self.submitBtn.draw()
        self.clearBtn.draw()
        self.alert.draw('Enter puzzle')

    def updateSquare(self, text):
        self.board.updateSelectedSq(text)

    def moveSelected(self, dirMove):
        self.board.moveSelected(dirMove)

    def checkClick(self, mPos):
        self.board.unselectAll()
        self.board.checkForClickedSquare(mPos)

        if self.submitBtn.checkIfClicked(mPos):
            self.alert.draw('Solving...')
            s = self.board.solve()
            if not s:
                self.alert.draw('Unsolvable')

        elif self.clearBtn.checkIfClicked(mPos):
            self.board.clear()
            self.alert.draw('Enter puzzle')


def main():
    g = game()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    g.moveSelected(0)
                elif event.key == pygame.K_RIGHT:
                    g.moveSelected(1)
                elif event.key == pygame.K_UP:
                    g.moveSelected(2)
                elif event.key == pygame.K_DOWN:
                    g.moveSelected(3)

                # Ensure that there is a selected square
                if g.selectedSqCoord != None:
                    text = event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        text = ''
                    if text in '123456789':
                        g.updateSquare(text)

            if event.type == pygame.MOUSEBUTTONUP:
                mPos = pygame.mouse.get_pos()
                g.checkClick(mPos)

        # Draw background
        setup.WIN.fill([255, 255, 255])

        # Render board
        g.render()
        pygame.display.update()

    pygame.quit()


main()
