from Notes import*

class SpecialNote(Notes):
    def __init__(self, xPos, noteSize, time, songbpm, app):
        super().__init__(0, noteSize, time, songbpm, app)