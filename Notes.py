################################################################################
# This is the parent Notes class which will contain the following values for each note (game element)
# -x position   
# -y position
# -a noteLength (if the note is a slider, how long the slider is)
# -score(the score value of the note)
# -noteSize (a scaling factor depending on the size of the display)
# -noteTime (the time which the note first appears)
# -scoreTime (the time when the note is checked if it is scored or not)
################################################################################
class Notes(object):
    def __init__ (self, xPos, noteSize, timeOnScreen, app, score = 20):
        #Note Display Information###############################################
        self.color = "red"
        self.timeOnScreen = timeOnScreen        
        self.x, self.y = xPos, -noteSize #Note Starting Position
        self.noteSize = noteSize
        ########################################################################
        #Note Scoring attributes################################################
        self.scoreHeight = app.height*0.9
        self.score = score
        self.scored = False
        self.scoreTolerance = app.height/20
        ########################################################################
    
    #Function draws the note's current position#################################
    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        r = self.noteSize
        x0, x1 = cx, cx + r
        y0, y1 = cy - r/4, cy + r/4
        canvas.create_rectangle(x0, y0, x1, y1, fill = self.color)
    ############################################################################

    #This function moves the note down on the screen based on the time since the last timerFired
    def updateNotePos(self, app, dt, difficulty):
        self.y += app.height * difficulty * dt/self.timeOnScreen
    ############################################################################

    #Function takes in player input and matches it with the note's x-position,
    def scoreNote(self):
        if not self.scored and abs(self.y-self.scoreHeight) < self.scoreTolerance:
            self.scored = True
            self.color = "dark grey" #set note to grey to indicate scoring
            return self.score
        return 0
        ########################################################################
################################################################################
class Node(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(xPos, noteSize, timeOnScreen, app)

    def getImage(self, app):
        return app.loadImage('')
    
    def scoreNote(self, playerInputs):
        for input in playerInputs:
            if self.x == input:
                return super().scoreNote()
        return 0
################################################################################
class Slider(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app, noteLength):
        super().__init__(xPos, noteSize, timeOnScreen, app)
        self.noteLength = noteLength
        self.scoreSections = [[self.y - i * noteSize, False] for i in range(noteLength)]

    #Overrides to move all sections of slider note down
    def updateNotePos(self, app, dt, difficulty):
        super().updateNotePos(app, dt, difficulty)
        for sec in self.scoreSections:
            sec[0] += app.height * difficulty * dt/self.timeOnScreen

    def scoreNote(self, playerInputs):
        for sec in self.scoreSections: #loops through all scoring sections of slider
            height, scored = sec[0], sec [1]
            for input in playerInputs: #loops through both player inputs
                if (not scored and self.x == input and 
                    abs(height - self.scoreHeight) < self.scoreTolerance):
                    self.color = "dark grey"
                    sec[1] = True
                    return self.score
        return 0

    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - (self.noteLength*r), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = self.color)

#New Parent class for "Special Notes" (notes with widths of the entire board)###
class SpecialNote(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)

    def drawNote(self, canvas, offset, width):
        cy,r  = self.y, self.noteSize
        x0, x1 = offset, offset + width
        y0, y1 = cy - r/4, cy + r/4
        canvas.create_rectangle(x0, y0, x1, y1, fill = self.color)

#SUBCLASS OF SPECIALNOTES#######################################################
class Jump(SpecialNote):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)
        self.color = "blue"
        
    def drawNote(self, canvas, offset, width):
        super().drawNote(canvas, offset, width)

    def scoreNote(self, playerInputs):
        if len(playerInputs) == 0:
            return super().scoreNote()
        return 0

#SUBCLASS OF SPECIALNOTES#######################################################
class Down(SpecialNote):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)
        self.color = "yellow"

    def drawNote(self, canvas, offset, width):
        super().drawNote(canvas, offset, width)

    def scoreNote(self, inputs, oldInputs):
        if len(inputs) > 0 and () in oldInputs:
            return super().scoreNote()
        return 0