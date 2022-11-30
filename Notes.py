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
        self.scoreTolerance = app.height/20

        self.timeOnScreen = timeOnScreen
        
        #Note Starting Position
        self.x, self.y = xPos, -noteSize
        
        #Note size attribute
        self.noteSize = noteSize

        #Score and times
        self.score = score
        self.scoreHeight = app.height*0.9

        self.scored = False

#Function draws the note's current position
    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - r/4, cy + r/4
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')


#This function moves the note down on the screen
    def updateNotePos(self, app, dt, difficulty):
        self.y += app.height * difficulty * dt/self.timeOnScreen


#Function takes in player input and matches it with the note's x-position,
    def scoreNote(self):
        if not self.scored and abs(self.y-self.scoreHeight) < self.scoreTolerance:
            self.scored = True
            return self.score
        return 0

class Node(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(xPos, noteSize, timeOnScreen, app)

    def scoreNote(self, playerInputs):
        #Check player input algorithm later TODO
        #input1, input2 = playerInput[0], playerInput[1]
        for input in playerInputs:
            if self.x == input:
                return super().scoreNote()
        return 0

class Slider(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app, noteLength):
        super().__init__(xPos, noteSize, timeOnScreen, app)
        self.noteLength = noteLength
        #TODO Change the time interval that the slider spawns multiople nodes
        self.scoreSections = [[self.y - i * noteSize, False] for i in range(noteLength)]

    def updateNotePos(self, app, dt, difficulty):
        super().updateNotePos(app, dt, difficulty)
        for sec in self.scoreSections:
            sec[0] += app.height * difficulty * dt/self.timeOnScreen

    def scoreNote(self, playerInputs):
        #Check player input algorithm later TODO
        for sec in self.scoreSections:
            height, scored = sec[0], sec [1]
            for input in playerInputs:
                if (not scored and self.x == input and 
                    abs(height - self.scoreHeight) < self.scoreTolerance):
                    sec[1] = True
                    return self.score
        return 0

    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - (self.noteLength*r), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')

class SpecialNote(Notes):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)

    def drawNote(self, canvas, color, offset, width):
        
        cy = self.y
        r = self.noteSize

        canvas.create_rectangle(offset, cy - r/4, offset + width, cy + r/4, fill = color)

class Jump(SpecialNote):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)
        
    def drawNote(self, canvas, offset, width):
        color = "blue"
        super().drawNote(canvas, color, offset, width)

    def scoreNote(self, playerInputs):
        #Check player input algorithm later TODO
        if len(playerInputs) == 0:
            return super().scoreNote()
        return 0

class Down(SpecialNote):
    def __init__(self, xPos, noteSize, timeOnScreen, app):
        super().__init__(0, noteSize, timeOnScreen, app)

    def drawNote(self, canvas, offset, width):
        color = "yellow"
        super().drawNote(canvas, color, offset, width)

    def scoreNote(self, inputs, oldInputs):
        #Check player input algorithm later TODO
        if len(inputs) > 0 and () in oldInputs:
            return super().scoreNote()
        return 0