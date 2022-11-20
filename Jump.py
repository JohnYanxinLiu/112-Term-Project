from cmu_112_graphics import *
from Notes import Notes

class Jump(Notes):
    def __init__(self, xPos, noteSize, time, songbpm):
        super().__init__(0, noteSize, time, songbpm, 1)
        
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