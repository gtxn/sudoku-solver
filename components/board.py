import pygame
from squares import square, miniGrid
from utils.solver import solve
from utils.setup import *

class board():
    def __init__(self):
        tmpBoardArr = []
        for j in range(9):
            tmpRow = []
            for i in range(9):
                s = square(SQUARESIZE)
                w, h = s.width, s.height
                s.xPos = ((WIDTH-10*w)/2) + i*w + w/2
                s.yPos = ((HEIGHT-10*h)/2) + j*h + h/2
                s.coord = [j, i]
                tmpRow.append(s)
            tmpBoardArr.append(tmpRow)

        tmpMiniGridArr = []
        for j in range(3):
            tmpRow = []
            for i in range(3):
                size = SQUARESIZE * 3
                gxPos = ((WIDTH-10*w)/2) + i*size + w/2
                gyPos = ((HEIGHT-10*h)/2) + j*size + h/2
                miniG = miniGrid(gxPos, gyPos)
                tmpRow.append(miniG)
            tmpMiniGridArr.append(tmpRow)

        self.boardArr = tmpBoardArr
        self.miniGArr = tmpMiniGridArr
        self.selectedSqCoord = [0, 0]

    def drawBoard(self):
        for row in self.miniGArr:
            for miniG in row:
                miniG.draw()

        for row in self.boardArr:
            for square in row:
                if square.coord == self.selectedSqCoord:
                    self.selectedSq = square
                    square.selected = True

                square.draw()

    def bToArray(self):
        boardArr = []
        for row in self.boardArr:
            tmpRow = []
            for elem in row:
                if elem.number == '':
                    tmpRow.append(0)
                else:
                    tmpRow.append(int(elem.number))
            boardArr.append(tmpRow)

        return boardArr

    def solve(self):
        bArr = self.bToArray()
        isSolved = solve(bArr)
        
        if isSolved:
            self.selectedSqCoord = None
            for row in range(len(bArr)):
                for col in range(len(bArr[row])):
                    self.boardArr[row][col].number = str(bArr[row][col])
            return True

        return False

    def clear(self):
        for row in self.boardArr:
            for sq in row:
                sq.number = ''

    def unselectAll(self):
        for row in self.boardArr:
            for square in row:
                square.selected = False

    def checkForClickedSquare(self, mPos):
        for row in self.boardArr:
            for square in row:
                r = square.getRect()
                if r.collidepoint(mPos):
                    self.selectedSqCoord = square.coord

    def updateSelectedSq(self, num):
        for row in self.boardArr:
            for square in row:
                if square.coord == self.selectedSqCoord:
                    square.number = num

    def moveSelected(self, mvDir):
        self.unselectAll()
        # dir 0, 1, 2, 3 => L, R, U, D
        dirVector = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        finCo = [self.selectedSqCoord[0]+dirVector[mvDir][0],
                 self.selectedSqCoord[1]+dirVector[mvDir][1]]
        if finCo[0] >= 0 and finCo[0] < 9 and finCo[1] >= 0 and finCo[1] < 9:
            self.selectedSqCoord = finCo
