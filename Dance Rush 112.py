from cmu_112_graphics import *
import Node
import Note


class Game (object):
    def __init__(self):
        self.note = Node(100)

    
    def timerFired(self):
        self.note.updateNotePos()

    def redrawAll(self, canvas):
        self.note.drawNote(canvas)
