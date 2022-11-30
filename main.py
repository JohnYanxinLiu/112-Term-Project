from cmu_112_graphics import *
from Notes import *
from Player import *
from Map import *
import time
import math

def appStarted(app):
    
    app.difficulty = 4
    app.timerDelay = 10
    app.bpm = 30

    app.beatsPerSec = app.bpm/60
    app.timeOnScreen = 2
    app.notesMoving = 12 * (app.beatsPerSec * app.timeOnScreen + 1)
    app.ticksOnScreen = app.timeOnScreen * 1000/app.timerDelay

    
    app.map = Map(app, 50, app.ticksOnScreen, 1)
    app.notesMap = app.map.notesMap
    app.player = Player()
    app.gameTick = 0
    app.gameBeat = 0

    app.lastSecond = time.time()
    app.tOld = time.time()
    app.tNew = time.time()
    app.dt = app.tOld-app.tNew
    
def timerFired(app):
    #Updates the current beat the game is on####################################
    if (math.isclose(time.time() - app.lastSecond, app.beatsPerSec) 
                  or time.time() - app.lastSecond > app.beatsPerSec):
        app.gameBeat += 1
        app.lastSecond = time.time()
    ############################################################################

    #Time value used for updating note positions################################
    app.tNew = time.time()
    dt = app.tNew-app.tOld
    app.tOld = app.tNew
    ############################################################################

    #Loops through all notes####################################################

    #Obtains range of keys of notes which will be moved in for loop 
    noteKeyRange = returnMovingNotesRange(app)    

    for key in noteKeyRange:
        note = app.notesMap[key]
        
        #Updates the position of each note
        note.updateNotePos(app, dt, app.difficulty)
        
        score = 0
        #Special scoring method for Slider Note
        if type(note) == Slider:        
            for node in note.scoringNodes:
                score = node.scoreNote(app.player.getInputs())
                app.player.updateScore(score)
            continue
        #Special scoring method for Down, we pass in old inputs too
        elif type(note) == Down:
            score = note.scoreNote(app.player.getInputs(), app.player.oldInputs)
            #Default scoring method
        else: 
            score = note.scoreNote(app.player.getInputs())
        app.player.updateScore(score)
            
    app.player.updateOldInputs(app.player.inputs)

def returnMovingNotesRange(app):
    initialBeat = app.gameBeat - int(app.notesMoving)
    finalBeat = app.gameBeat + int(app.notesMoving)
    
    #Clips the initial and final beat to not go out of the bounds of the notes map dictionary
    if initialBeat < 0:
        initialBeat = 0
    if finalBeat > app.map.mapLen:
        finalBeat = app.map.mapLen
    
    return range(initialBeat, finalBeat)
    

def keyPressed(app, event):
    app.player.holdKey(event)

def keyReleased(app, event):
    app.player.releaseKey(event)

def redrawAll(app, canvas):
    app.map.drawGame(canvas)
    app.player.drawScore(canvas)
    app.player.drawInputs(canvas, app.height, app.map.lBorder, app.map.cellWidth)

runApp(width=500, height=500)
