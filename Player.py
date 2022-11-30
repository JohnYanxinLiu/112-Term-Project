################################################################################
# Player object controls player score and player input
################################################################################

class Player(object):
    def __init__(self):
        self.score = 0
        #inputs will be a list of 2 x-positions
        self.inputs = set()
        self.score = 0
        self.oldInputs = []

    def getInputs(self):
        return self.inputs

    def holdKey(self, event):
        #Checks that the key pressed is a digit and that there will be no more than 2 inputs
        if event.key.isdigit() and len(self.inputs) <2:
            #For ergonomics, 0 = 10
            if event.key == '0':
                self.inputs.add(10)
            else:
                self.inputs.add(int(event.key))

    def releaseKey(self, event):
        #If the key released is 0, remove 10
        if event.key == '0':
                self.inputs.remove(10)
        #if the key released is a digit and the digit is in the set of inputs, remove the input
        if event.key.isdigit() and int(event.key) in self.inputs:
            self.inputs.remove(int(event.key))
    
    def drawScore(self, canvas):
        canvas.create_text(100, 50, text = str(self.score))
    
    def drawInputs(self, canvas, height, lBorder, cellWidth):
        y0, y1 = height * 0.90, height * 0.91
        for x in self.inputs:
            x -= 1
            x0 = lBorder + x * cellWidth
            x1 = x0 + cellWidth
            canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')


    def updateOldInputs(self, newInputs):
        inputs = tuple(newInputs)
        self.oldInputs.append(inputs)
        if len(self.oldInputs) > 5:
            self.oldInputs.pop(0)


    def updateScore(self, score):
        if score != None:
            self.score += score