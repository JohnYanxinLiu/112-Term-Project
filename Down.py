from cmu_112_graphics import *
from Notes import Notes
from Special_Note import*

class Down(Special_Note):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)