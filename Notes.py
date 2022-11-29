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
    def __init__ (self, xPos, noteSize, time, songbpm, app, score = 20):
        #Note Starting Position
        self.x, self.y = xPos, -noteSize
        
        #Note size attribute
        self.noteSize = noteSize
        
        #Score and times
        self.score = score
        self.noteTime = time
        timeOnBoard = 10 * songbpm
        self.scoreTime = time + timeOnBoard

        self.dy = app.height/timeOnBoard

        self.scored = False

#Function draws the note's current position
    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - r/4, cy + r/4
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')


#This function moves the note down on the screen
    def updateNotePos(self, gameTime):
        if gameTime >= self.noteTime:
            self.y += self.dy


#Function takes in player input and matches it with the note's x-position,
    def scoreNote(self, scored):
        if scored:
            self.scored = True
            return self.score
        else:
            return 0

class Node(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(xPos, noteSize, time, songbpm, app)

    def scoreNote(self, playerInputs, time):
        #Check player input algorithm later TODO
        #input1, input2 = playerInput[0], playerInput[1]
        if abs(time - self.scoreTime) > 2:
            return 0
        for input in playerInputs:
            if self.x == input and not self.scored:
                return super().scoreNote(True)
        #return 0 if the player input is not close enough
            if not self.scored:
                return super().scoreNote(False)
        return 0

class Slider(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app, noteLength):
        super().__init__(xPos, noteSize, time, songbpm, app, noteLength)
        #noteLength is randomly generated from Map class and passed through
        self.noteLength = noteLength
        '''timeInterval = noteLength * songbpm'''
        #TODO Change the time interval that the slider spawns multiople nodes
        self.scoringNodes = [(Node(xPos, noteSize, time + i, songbpm, app)) for i in range(noteLength)]


    def scoreNote(self, playerInput, time):
        #Check player input algorithm later TODO
        for node in self.scoringNodes:
            score = node.scoreNote(playerInput, time)
            if score != 0:
                self.scoringNodes.pop(0)
                return score


    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - (self.noteLength*r/2), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')

class SpecialNote(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)

    def drawNote(self, canvas, color, offset, width):
        
        cy = self.y
        r = self.noteSize

        canvas.create_rectangle(offset, cy - r/4, offset + width, cy + r/4, fill = color)

class Jump(SpecialNote):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)
        
    def drawNote(self, canvas, offset, width):
        color = "blue"
        super().drawNote(canvas, color, offset, width)

    def scoreNote(self, playerInputs, time):
        #Check player input algorithm later TODO
        if abs(time - self.scoreTime) > 1:
            return
        if len(playerInputs) == 0 and not self.scored:
                super().scoreNote(True)
                return self.score
        #return 0 if the player input is not close enough
        if not self.scored:
                super().scoreNote(False)
                return 0

class Down(SpecialNote):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)

    def drawNote(self, canvas, offset, width):
        color = "yellow"
        super().drawNote(canvas, color, offset, width)

    def scoreNote(self, inputs, time, oldInputs):
        #Check player input algorithm later TODO
        if abs(time - self.scoreTime) > 6:
            return 0
        if len(inputs) > 0 and () in oldInputs and not self.scored:
            super().scoreNote(True)
            return self.score
        #return 0 if the player input is not close enough
        if not self.scored:
            super().scoreNote(False)
            return 0