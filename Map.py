from Notes import *
from Node import *
from Jump import *
from Slider import *
import random

class Map(object):

    def __init__(self, mapLength, bpm, difficulty):
        skip = 0
        
        self.notesMap = [Node(100, 20, 15, 20), Slider(200, 20, 5, 5, 10), Jump(0, 20, 30, 30)]

    '''def randomNote(self):
        noteType = random.randint(1,3)
        
        if noteType == 1:
            return Node(attributes)
        if noteType == 2:
            return Jump(attribute)
        if noteType == 3:
            return Slider(attribute)'''