class Notes(object):
    def __init__ (self, xPos, noteSize, time, songbpm, score = 20, noteLength = 1):
        self.x = xPos
        self.noteLength = noteLength
        self.y = -noteSize
        self.score = score
        self.noteSize = noteSize
        self.noteTime = time
        self.scoreTime = time + songbpm


#Function draws the note's current position
    def drawNote(self, canvas):
        cx, cy = self.x, self.y
        r = self.noteSize
        canvas.create_rectangle(cx - r, cy - r/2, cx + r, cy + r/2, fill = 'red')


    def updateNotePos(self, gameTime):
        if gameTime >= self.noteTime:
            self.y += 1


#Function takes in player input and matches it with the note's x-position,
    def scoreNote(self, playerInput):
        #Check player input algorithm later TODO
        input1, input2 = playerInput[0], playerInput[1]
        if self.x == input1 or self.x == input2:
            return self.score
        #return 0 if the player input is not close enough
        return 0  