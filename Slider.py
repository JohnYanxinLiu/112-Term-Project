from cmu_112_graphics import *
from Node import *
from Notes import *

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
            score = node.scoreNote(playerInput, node.scoreTime)
            if score != 0:
                self.scoringNodes.pop(0)
                return score


    def drawNote(self, canvas, offset, cellWidth):
        cx, cy = (self.x - 1)*cellWidth + offset, self.y
        
        r = self.noteSize
        
        x0, x1 = cx, cx + r
        y0, y1 = cy - (self.noteLength*r/2), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')