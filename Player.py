from cmu_112_graphics import *
################################################################################
# Player object controls player score and player input
################################################################################

class Player(object):
    def __init__(self, app, numKeys, cellWidth):
        self.numKeys = numKeys
        #inputs will be a list of 2 x-positions
        self.inputs = set()
        self.score = 0
        self.oldInputs = []
        #keyPressImg image obtained from https://osu.ppy.sh/community/forums/topics/807428?n=1
        keyPressImg = app.loadImage('keyPressImage.png')
        self.keyPressImage = keyPressImg.resize((int(cellWidth) + 20//numKeys, int(app.height)*2), Image.ANTIALIAS)

    def getInputs(self):
        return self.inputs

    #Function creates a set of keys that are held by the player#################
    def holdKey(self, event):
        key = event.key
        #Checks that the key pressed is:
        #   a digit
        #   will have no more than 2 inputs
        #   will be within the bounds of numKeys
        if key.isdigit() and len(self.inputs) <2 and int(key) <= self.numKeys:
            if key == '0' and self.numKeys >= 10: #For ergonomics, 0 = 10
                self.inputs.add(10)
            elif key == '0':
                pass
            else:
                self.inputs.add(int(key))

    #removes elements from the set with keys are released#######################
    def releaseKey(self, event):
        key = event.key
        if key == '0' and 10 in self.inputs: #If the key released is 0, remove 10
                self.inputs.remove(10)
        #if the key released is a digit and the digit is in the set of inputs, remove the input
        if key.isdigit() and int(key) in self.inputs:
            self.inputs.remove(int(key))
    
    def drawScore(self, canvas):
        canvas.create_text(50, 50, font = "Arial 15 bold", text = str(self.score), fill = "white")
    
    #Draws key press inputs#####################################################
    def drawInputs(self, canvas, height, lBorder, cellWidth):
        y = height * 0.95
        for x in self.inputs:
            x -= 1
            x = lBorder + x * cellWidth + cellWidth/2
            canvas.create_image(x, y, image=ImageTk.PhotoImage(self.keyPressImage))

    #Stores old inputs in a list and pops the 0th elem once it holds 5 inputs### 
    #Special Use: for Down Note#################################################
    def updateOldInputs(self, newInputs):
        inputs = tuple(newInputs)
        self.oldInputs.append(inputs)
        if len(self.oldInputs) > 5:
            self.oldInputs.pop(0)

    #Adds score to player score#################################################
    def updateScore(self, score):
        if score != None:
            self.score += score