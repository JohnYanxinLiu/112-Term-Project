from Notes import *
from cmu_112_graphics import *
import random
################################################################################
# Player object controls player score and player 
# Map class handles generating/managing all the notes and game visuals
################################################################################
class Map(object):
    def __init__(self, app, mapLength, timeOnScreen, difficulty, numCells):
        #Setting up the background and drawing
        ########################################################################
        self.numCells = numCells
        self.width, self.height = app.width, app.height
        margin = app.width // 5        
        self.lBorder, self.rBorder = margin, app.width - margin
        self.boardWidth = self.rBorder - self.lBorder
        self.cellWidth = (self.rBorder - self.lBorder)/self.numCells
        self.boardCoords = [(margin + i * self.cellWidth + 1/2 * self.cellWidth) for i in range(self.numCells+1)] #Add 1 to self.numCells because this gives 11 x coords for 10 cells (in between)
        
        #BackgroundImage obtained from https://phandroid.com/2020/06/29/best-rhythm-games-for-android-and-iphone/
        #Board cell image obtained from https://osu.ppy.sh/community/forums/topics/807428?n=1
        bgImage = app.loadImage('backgroundImgS.png')
        boardCellImage = app.loadImage('inputoverlay-background.png')
        #Learned how to resize from https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter
        self.boardCellImage = boardCellImage.resize((int(self.cellWidth) + 20//self.numCells, int(app.height*4/3)), Image.ANTIALIAS)
        self.bgImage = app.scaleImage(bgImage, 1.5)
        
        #Generates Notes Map
        ########################################################################
        self.difficulty = difficulty
        self.mapLen = mapLength
        self.timeOnScreen = timeOnScreen
        self.leftNotesMap = dict()
        self.rightNotesMap = dict()
        
        self.generateLeftMap(app)
        self.generateRightMap(app)

        ########################################################################

    #Generates the first map
    ############################################################################
    def generateLeftMap(self, app):
        skip = 0
        prevNote = None
        for beat in range(self.mapLen):
            #Skips over beats if there was a slider
            if skip > 0:
                skip -= 1
                continue
            #generates a note
            note = self.randomNote(app)
            
            #Does not place another SpecialNote if the previous note was a SpecialNote
            if prevNote != None:
                while (isinstance(prevNote, SpecialNote) and isinstance(note, SpecialNote)):
                    note = self.randomNote(app)

            #Skips over beats with sliders
            if type(note) == Slider:
                skip = note.noteLength

            
            self.leftNotesMap [beat] = note
            prevNote = note

    #Generates a simultaneous map of just nodes
    ############################################################################
    def generateRightMap(self, app):
        chance = self.difficulty/2 + 1
        for beat in range(self.mapLen):
            note = self.randomNode(app)

            #randomness aspect of whether a note should be placed or not
            placeNote = random.randint(0,int(chance))
            if placeNote < 2: continue

            #In the case of sliders, obtain the x value of the slider
            if beat not in self.leftNotesMap:
                oldNoteX = self.leftNotesMap[self.returnSliderBeat()].x
                self.rightNotesMap [beat] = note
                continue
            else:
            #else, obtain the x value of the simultaneous note
                oldNoteX = self.leftNotesMap[beat].x
            newNoteX = note.x
            
            #Don't place a node at the same time as a SpecialNote
            if isinstance(oldNoteX, SpecialNote):
                continue

            #Generate a new not if the notes overlap
            while oldNoteX == newNoteX:
                note = self.randomNode(app)
                oldNoteX = self.leftNotesMap[beat].x
                newNoteX = note.x
            self.rightNotesMap [beat] = note

    def returnSliderBeat(self):
        key = len(self.leftNotesMap)
        while key not in self.leftNotesMap:
            key -= 1
        return key


    def randomNode(self, app):
        noteSize = self.cellWidth
        xPos = random.randint(1 ,self.numCells)
        return Node(xPos, noteSize, self.timeOnScreen, app)
        
    def randomNote(self, app):
        noteType = random.randint(1, 10)
        noteSize = self.cellWidth
        xPos = random.randint(1 ,self.numCells)
        if noteType >= 8:
            length = random.randint(2,6)
            return Slider(xPos, noteSize, self.timeOnScreen, app, length)
        if 3 <= noteType < 8:
            return Node(xPos, noteSize, self.timeOnScreen, app)
        if noteType == 2:
            return Jump(0, noteSize, self.timeOnScreen, app)
        if noteType == 1:
            return Down(0, noteSize, self.timeOnScreen, app)

    def drawNotes(self, canvas, offset, notesMap):
        for beat in notesMap:
            note = notesMap[beat]
            if isinstance(note, SpecialNote):
                noteWidth = self.boardWidth
            else: 
                noteWidth = self.cellWidth
            note.drawNote(canvas, offset, noteWidth)

    def drawGame(self, canvas):
        self.drawBackground(canvas)
        self.drawBoard(canvas)
        self.drawNotes(canvas, self.lBorder, self.rightNotesMap)
        self.drawNotes(canvas, self.lBorder, self.leftNotesMap)


    def drawStartScreen(self, canvas):
        self.drawBackground(canvas)
        x, y = self.width/2, self.height/2
        startMessage = '''
        Welcome to Dance Rush 112!! \n
            (Press any key to play)'''
        canvas.create_text(x, y, text = startMessage, font = "Arial 15 bold", fill = "white")
    

    def drawBackground(self, canvas):
        canvas.create_image(self.width//2, self.height//2, image=ImageTk.PhotoImage(self.bgImage))


    #Draws the game board that the notes come down on
    def drawBoard(self, canvas):
        self.numCells 
        for i in range(len(self.boardCoords) - 1):
            canvas.create_image(self.boardCoords[i], self.height*3/5, image=ImageTk.PhotoImage(self.boardCellImage))
