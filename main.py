from cmu_112_graphics import *
from Notes import *
from Player import *
from Map import *
import time
import math

def appStarted(app):
    #in-Game Info###############################################################
    app.difficulty = 2
    app.timerDelay = 10
    app.bpm = 10
    app.numCells = 8
    app.timeOnScreen = 3
    app.mapLength = 200
    app.difficulty = 3
    ############################################################################

    #Calculated game info#######################################################
    app.beatsPerSec = app.bpm*60
    app.secPerBeat = app.bpm/60
    app.notesMoving = app.secPerBeat * app.timeOnScreen
    ############################################################################

    #Create Notes Map###########################################################
    app.map = Map(app, app.mapLength, app.timeOnScreen, app.difficulty, app.numCells)
    app.leftNotesMap = app.map.leftNotesMap
    app.rightNotesMap = app.map.rightNotesMap
    ############################################################################

    #Initialize Player##########################################################
    app.player = Player(app, app.numCells, app.map.cellWidth)
    ############################################################################

    #Initialize time variables used every tick##################################
    app.gameBeat = 0
    app.lastSecond = time.time()
    app.tOld = time.time()
    app.tNew = time.time()
    app.dt = app.tOld-app.tNew

    app.gameStarted = False

def timerFired(app):
    if not app.gameStarted: return #don't begin the game until the game is started
    updateGameBeat(app)    
    updateGameTime(app)
    movingNotesKeys = returnMovingNotesRange(app) #Obtains range of keys of notes which will be moved in for loop 
    updateNotes(app, app.rightNotesMap, movingNotesKeys, app.dt)
    updateNotes(app, app.leftNotesMap, movingNotesKeys, app.dt)


    app.player.updateOldInputs(app.player.inputs)

#Helper function updates the current beat the game is on########################
def updateGameBeat(app):
    if (math.isclose(time.time() - app.lastSecond, app.secPerBeat) 
                  or time.time() - app.lastSecond > app.secPerBeat):
        app.gameBeat += 1
        app.lastSecond = time.time()

#Helper Function updates time values used for note positions####################
def updateGameTime(app):
    app.tNew = time.time()
    app.dt = app.tNew-app.tOld
    app.tOld = app.tNew

#Helper function scores and updates position of notes###########################
def updateNotes(app, map, keys, dt):
    for key in keys: #Loops through all the moving notes
        if key not in map:
            continue #Accounts for sliders taking out beats

        note = map[key]
        note.updateNotePos(app, dt, app.difficulty) #Updates the position of each note
        
        score = 0
        if type(note) == Down: #Need to pass old inputs to score Down note
            score = note.scoreNote(app.player.getInputs(),
                                   app.player.oldInputs)
        else: 
            score = note.scoreNote(app.player.getInputs())
        app.player.updateScore(score)


#Helper function returns the keys of only the notes that are moving at a specific point in the game to reduce lag
def returnMovingNotesRange(app):
    initialBeat = app.gameBeat - int(app.notesMoving) - 20 #experimentally found a lower initialBeat key is needed
    finalBeat = app.gameBeat + int(app.notesMoving)
    
    #Clips the initial and final beat to not go out of the bounds of the notes map dictionary
    if initialBeat < 0:
        initialBeat = 0
    if finalBeat >= app.map.mapLen:
        finalBeat = app.map.mapLen
    
    return range(initialBeat, finalBeat)

def keyPressed(app, event):
    app.player.holdKey(event)
    if event.key.isalpha:
        app.gameStarted = True

def keyReleased(app, event):
    app.player.releaseKey(event)

def redrawAll(app, canvas):
    if not app.gameStarted:
        app.map.drawStartScreen(canvas)
    else:
        app.map.drawGame(canvas)
        app.player.drawScore(canvas)
        app.player.drawInputs(canvas, app.height, app.map.lBorder, app.map.cellWidth)

runApp(width=600, height=500)
