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
            input = 1
        elif event.key == '2':
            input = 2
        elif event.key == '3':
            input = 3
        elif event.key == '4':
            input = 4
        elif event.key == '5':
            input = 5
        elif event.key == '6':
            input = 6
        elif event.key == '7':
            input = 7
        elif event.key == '8':
            input = 8
        elif event.key == '9':
            input = 9
        elif event.key == '0':
            input = 10
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