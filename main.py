from classes.Song import *
from classes.Playlist import *

song1 = Song("Girl of the year","Beach House",3,51,Genre.DREAM_POP) 
song2 = Song("Silver Soul","Beach Hosue",4,58,Genre.DREAM_POP)
song3 = Song("La carretera nocturna","Triángulo de amor bizarro",3,24,Genre.INDIE)
song4 = Song("Elevator Song","Keaton Henson",3,50,Genre.PIANO)

pl = Playlist("This is Beach House!",[song1,song2,song3])
"""
print("The longest song in "+pl.title+" playlist is "+pl.getLongestSong().name)


print("Songs of Dream Pop are:")
dreampop_songs = pl.getSongsByGenre(Genre.DREAM_POP)
for song in dreampop_songs:
    print(song.name)
"""

#pl.play()

#pl.addSong(song4)
pl.play()
pl.deleteSong(song1)
pl.play()