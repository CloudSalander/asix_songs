from enum import Enum

class Genre(Enum):
    DREAM_POP = 1
    INDIE = 2
    PIANO = 3

class Song:
    def __init__(self,name,author,minutes,seconds,genre):
        self.name = name
        self.author = author
        self.minutes = minutes
        self.seconds = seconds
        self.genre = genre
    
    def play(self):
        print("Reproduciendo "+self.name+" ...")