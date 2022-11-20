################################################################################
# Player object controls player score and player input
################################################################################

class Player(object):
    def __init__(self):
        self.score = 0
        #self.inputs will be a list of 2 x-positions
        self.inputs = [None]

    def playerInputs(self):
        return [self.inputs[0], self.inputs[1]]

    def updatePlayerInputs(self, event, x0 = -1, x1 = -1):
        if event.key == '1':
            self.inputs = [1]
        elif event.key == '2':
            self.inputs = [2]
        elif event.key == '3':
            self.inputs = [3]
        elif event.key == '4':
            self.inputs = '4'
        else:
            self.inputs = None
        return False

    def setDefaultInput(self):
        self.inputs = [None]
        