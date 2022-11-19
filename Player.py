class Player(object):
    def __init__(self):
        self.score = 0
        #self.inputs will be a list of 2 x-positions
        self.inputs = []

    def playerInputs(self):
        return [self.inputs[0], self.inputs[1]]

    def updatePlayerInputs(self, event, x0 = None, x1 = None):
        x0, x1 = self.recordKeysPressed(event, x0, x1, event.key)


    def recordKeysPressed(self, event, x0, x1, playerInput, output):
        if x0 == None and x1 == None:
            return False
        if event.key == playerInput and x0 !=None:
            return x0, output
        elif event.key == playerInput:
            return output, None