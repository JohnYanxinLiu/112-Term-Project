class Background (object):
    def __init__(self, app):
        self.width = app.width
        self.height = app.height

#TODO Change this to use an image instead
    def drawGame(self, canvas):
        self.drawBackground(canvas)
        self.drawBoard(canvas)

    def drawBackground(self, canvas):
        x0, x1 = 0, self.width
        y0, y1 = 0, self.height
        canvas.create_rectangle(x0, y0, x1, y1, fill = "purple")

    def drawBoard(self, canvas):
