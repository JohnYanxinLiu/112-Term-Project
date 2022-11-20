from Node import *
from Slider import *


class Map(object):

    def __init__(self, mapLength, bpm, difficulty):
        self.notesMap = [Node(100, 20, 15, 20), Slider(200, 20, 5, 5, 10)]
