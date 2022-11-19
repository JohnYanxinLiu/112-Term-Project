from cmu_112_graphics import *
from Node import Node
from Notes import Notes

def appStarted(app):
    app.time = 0
    app.note = Node(100, 20, 50)
    
def timerFired(app):
    app.time += 1
    app.note.updateNotePos(app.time)

def redrawAll(app, canvas):
    app.note.drawNote(canvas)

runApp(width=1000, height=500)
