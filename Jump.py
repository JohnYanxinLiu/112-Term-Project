from cmu_112_graphics import *
from Notes import Notes
from Special_Note import*

class Jump(Special_Note):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)
        
    def drawNote(self, canvas):
        cy = self.y
        r = self.noteSize

        canvas.create_rectangle(0, cy - r, 500, cy + r, fill = 'blue')

    def scoreNote(self, playerInput):
        #Check player input algorithm later TODO
        if playerInput == None:
            return self.score
        #return 0 if the player input is not close enough
        return 0  