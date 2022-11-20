from Notes import*

class SpecialNote(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)

    def drawNote(self, canvas, color, offset, width):
        
        cy = self.y
        r = self.noteSize

        canvas.create_rectangle(offset, cy - r, offset + width, cy + r, fill = color)