from cmu_112_graphics import *
from Notes import *

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
                super().scoreNote(True)
                return self.score
        #return 0 if the player input is not close enough
            if not self.scored:
                super().scoreNote(False)
                return 0