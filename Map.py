from Notes import *
import random

class Map(object):
    numCells = 10
    def __init__(self, app, mapLength, timeOnScreen, difficulty):
        #Setting up the background and drawing
        ########################################################################
        self.width, self.height = app.width, app.height
        margin = app.width // 5        
        self.lBorder, self.rBorder = margin, app.width - margin
        self.boardWidth = self.rBorder - self.lBorder
        self.cellWidth = (self.rBorder - self.lBorder)/Map.numCells
        self.boardCoords = [(margin + i * self.cellWidth) for i in range(Map.numCells+1)] #Add 1 to Map.numCells because this gives 11 x coords for 10 cells (in between)
        
        #Generates Notes Map
        ########################################################################
        self.mapLen = mapLength
        self.timeOnScreen = timeOnScreen
        self.notesMap = dict()
        #self.notesMap = {0:Node(1, self.cellWidth, self.timeOnScreen, app), 1:Node(1, self.cellWidth, self.timeOnScreen, app)}
        for beat in range(mapLength):
            self.notesMap [beat] =  self.randomNote(app)            
        ########################################################################
        

    def randomNote(self, app):
        noteType = random.randint(1, 10)
        noteSize = self.cellWidth
        if noteType >= 8:
            xPos = random.randint(1 ,10)
            length = random.randint(2,4)
            return Slider(xPos, noteSize, self.timeOnScreen, app, length)
        if 3 <= noteType < 8:
            xPos = random.randint(1 ,10)
            return Node(xPos, noteSize, self.timeOnScreen, app)
        if noteType == 2:
            return Jump(0, noteSize, self.timeOnScreen, app)
        if noteType == 1:
            return Down(0, noteSize, self.timeOnScreen, app)

    def drawNotes(self, canvas, offset):
        for beat in self.notesMap:
            note = self.notesMap[beat]
            if isinstance(note, SpecialNote):
                noteWidth = self.boardWidth
            else: 
                noteWidth = self.cellWidth
            note.drawNote(canvas, offset, noteWidth)

    #TODO Change this to use an image instead
    def drawGame(self, canvas):
        self.drawBackground(canvas)
        self.drawBoard(canvas)
        self.drawNotes(canvas, self.lBorder)

#Currently draws the simple purple background of the game TODO Change to actual game background
    def drawBackground(self, canvas):
        x0, x1 = 0, self.width
        y0, y1 = 0, self.height
        canvas.create_rectangle(x0, y0, x1, y1, fill = "purple")

#Draws the musical board that the notes come down on
    def drawBoard(self, canvas):
        Map.numCells 
        y0, y1 = 0, self.height
        for i in range(len(self.boardCoords) - 1):
            x0, x1 = self.boardCoords[i], self.boardCoords [i+1]
            canvas.create_rectangle(x0, y0, x1, y1, fill = "grey", outline = "black")
