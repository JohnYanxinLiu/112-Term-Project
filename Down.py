from cmu_112_graphics import *
from Notes import Notes
from Special_Note import *

class Down(SpecialNote):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)

    def drawNote(self, canvas, offset, width):
        color = "yellow"
        super().drawNote(canvas, color, offset, width)

    def scoreNote(self, inputs, oldInputs):
        #Check player input algorithm later TODO
        if len(inputs) > 0 and () in oldInputs and not self.scored:
            super().scoreNote(True)
            return self.score
        #return 0 if the player input is not close enough
        if not self.scored:
            super().scoreNote(False)
            return 0