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
    def __init__ (self, xPos, noteSize, time, songbpm, noteLength = 1, score = 20):
        #Note Starting Position
        self.x, self.y = xPos, -noteSize
        
        #Note size attributes
        self.noteLength = noteLength
        self.noteSize = noteSize
        
        #Score and times
        self.score = score
        self.noteTime = time
        self.scoreTime = time + songbpm


#Function draws the note's current position
    def drawNote(self, canvas):
        cx, cy = self.x, self.y
        
        r = self.noteSize
        
        x0, x1 = cx - r, cx + r
        y0, y1 = cy - (self.noteLength*r/2), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')


#This function moves the note down on the screen
    def updateNotePos(self, gameTime):
        if gameTime >= self.noteTime:
            self.y += 5


#Function takes in player input and matches it with the note's x-position,
    def scoreNote(self, playerInput):
        #Check player input algorithm later TODO
        input1, input2 = playerInput[0], playerInput[1]
        if self.x == input1 or self.x == input2:
            return self.score
        #return 0 if the player input is not close enough
        return 0  