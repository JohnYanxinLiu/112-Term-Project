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
            print("scored")
            self.scored = True
            return self.score
        else:
            return 0

        