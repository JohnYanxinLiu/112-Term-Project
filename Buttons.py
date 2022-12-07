class Button():
    def __init__(self, cx, cy, bWidth, bHeight, color, text, func):
        self.func = func
        self.cx = cx
        self.cy = cy
        self.buttonHeight = bHeight
        self.buttonWidth = bWidth
        self.color = color
        self.text = text
        

    def runFunction(self):
        self.func()

    def isClicked(self, event):
        if (abs(self.cx - event.x) < self.buttonWidth and
            abs(self.cy - event.y) < self.buttonHeight):
            self.runFunction()

    def drawButton(self, canvas):
        x0, x1 = self.cx - self.buttonWidth, self.cx + self.buttonWidth
        y0, y1 = self.cy - self.buttonHeight, self.cy + self.buttonHeight
        canvas.create_rectangle(x0, y0, x1, y1, fill = self.color)

        # width = x1 - x0
        # height = y1 - y0
        # xInner0, xInner1 = x0 + 0.1*width, x1 - 0.1*width
        # yInner0, yInner1 = y0 + 0.1*height, y1 - 0.1*height
        # canvas.create_rectangle(x0,)