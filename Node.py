from cmu_112_graphics import *
from Notes import *

class Node(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(xPos, noteSize, time, songbpm, app)

    def scoreNote(self, playerInput, time):
        #Check player input algorithm later TODO
        #input1, input2 = playerInput[0], playerInput[1]
        input1 = playerInput
        if self.x == input1 and not self.scored:
            super().scoreNote(True)
        #return 0 if the player input is not close enough
        if not self.scored:
            super().scoreNote(False)