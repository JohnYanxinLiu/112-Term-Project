from Notes import *
from Node import *
from Jump import *
from Slider import *
import random

class Map(object):
    numCells = 10
    def __init__(self, app, mapLength, bpm, difficulty):
        
        self.width, self.height = app.width, app.height

        margin = app.width // 5
        self.lBorder, self.rBorder = margin, app.width - margin
        
        cellWidth = (self.rBorder - self.lBorder)/Map.numCells
        #Add 1 to Map.numCells because this gives 11 x coords for 10 cells (in between)
        self.boardCoords = [(margin + i * cellWidth) for i in range(Map.numCells+1)]

        skip = 0
        self.notesMap = [Node(100, 20, 15, 20), Slider(200, 20, 5, 5, 10), Jump(0, 20, 30, 30)]

    def randomNote(self):
        noteType = random.randint(1,3)
        xPos, noteSize, time, songbpm, noteLength = 1

        if noteType == 1:
            return Node(attributes)
        if noteType == 2:
            return Jump(attribute)
        if noteType == 3:
            return Slider(attribute)

#TODO Change this to use an image instead
    def drawGame(self, canvas):
        self.drawBackground(canvas)
        self.drawBoard(canvas)

    def drawBackground(self, canvas):
        x0, x1 = 0, self.width
        y0, y1 = 0, self.height
        canvas.create_rectangle(x0, y0, x1, y1, fill = "purple")

    def drawBoard(self, canvas):
        Map.numCells 
        y0, y1 = 0, self.height
        for i in range(len(self.boardCoords) - 1):
            x0, x1 = self.boardCoords[i], self.boardCoords [i+1]
            canvas.create_rectangle(x0, y0, x1, y1, fill = "grey", outline = "black")
