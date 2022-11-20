from cmu_112_graphics import *
from Notes import Notes
from Special_Note import*

class Jump(SpecialNote):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)
        
    def drawNote(self, canvas):
        color = "blue"
        super().drawNote(canvas, color)

    def scoreNote(self, playerInput, time):
        #Check player input algorithm later TODO
        if playerInput == None and not self.scored:
            super().scoreNote(True)
        #return 0 if the player input is not close enough
        if not self.scored:
            super().scoreNote(False)