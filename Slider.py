from cmu_112_graphics import *
from Notes import Notes

class Slider(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app, noteLength):
        super().__init__(xPos, noteSize, time, songbpm, app, noteLength)
        #noteLength is randomly generated from Map class and passed through
        self.noteLength = noteLength
        timeInterval = noteLength * songbpm
        #scoringSection list stores a list of lists [timesToScore, scored]
        self.scoringSection = [[timeInterval * i + self.noteTime, False] for i in range(noteLength)]

    def scoreNote(self, playerInput, time):
        #Check player input algorithm later TODO
        for section in self.scoringSection:
            timeToScore, sectionScored = section [0], section[1]
            if (playerInput == self.x 
                and not sectionScored 
                and abs(time - timeToScore) < 4):
                section [1] = True
                super().scoreNote(True)
            #return 0 if the player input is not close enough
            if not sectionScored:
                super().scoreNote(False)

    def drawNote(self, canvas):
        cx, cy = self.x, self.y
        r = self.noteSize
        
        x0, x1 = cx - r, cx + r
        y0, y1 = cy - (self.noteLength*r/2), cy + r/2
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')