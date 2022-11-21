################################################################################
# Player object controls player score and player input
################################################################################

class Player(object):
    def __init__(self):
        self.score = 0
        #self.inputs will be a list of 2 x-positions
        self.inputs = set()
        self.score = 0

    def getInputs(self):
        return self.inputs

    def holdKey(self, event):
        if event.key.isdigit() and len(self.inputs) <2:
           self.inputs.add(int(event.key))

    def releaseKey(self, event):
        if event.key.isdigit() and int(event.key) in self.inputs:
            self.inputs.remove(int(event.key))
            
    def drawScore(self, canvas):
        canvas.create_text(100, 50, text = str(self.score))
    
    def updateScore(self, score):
        if score != None:
            self.score += score