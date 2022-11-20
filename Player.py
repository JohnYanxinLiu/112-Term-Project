################################################################################
# Player object controls player score and player input
################################################################################

class Player(object):
    def __init__(self):
        self.score = 0
        #self.inputs will be a list of 2 x-positions
        self.inputs = [None, None]
        self.score = 0

    def playerInputs(self):
        return [self.inputs[0], self.inputs[1]]

    def updatePlayerInputs(self, event, side, x0 = -1, x1 = -1):
        if side:
            x0 = self.setInput(event, x0)
        elif not side:
            x1 = self.setInput(event, x1)
        self.inputs = [x0, x1]

    def setInput(self, event, input):
        if event.key == '1':
            input = [100]
        elif event.key == '2':
            input = [200]
        elif event.key == '3':
            input = [300]
        elif event.key == '4':
            input = '4'
        else:
            input = -1
        return input

    def setDefaultInput(self):
        self.inputs = [None]

    def drawScore(self, canvas):
        canvas.create_text(100, 50, text = str(self.score))
    
    def updateScore(self, score):
        if score != None:
            self.score += score