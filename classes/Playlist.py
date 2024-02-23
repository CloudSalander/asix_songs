class Playlist:
    def __init__(self,title,songs = []):
        self.title = title
        self.songs = songs
    
    def getLongestSong(self):
        max_seconds = 0
        longest_song = None
        for song in self.songs:
            if (song.minutes*60 + song.seconds) > max_seconds:
                max_seconds = song.minutes*60 + song.seconds
                longest_song = song
        return longest_song

    def getSongsByGenre(self,genre):
        songs = []
        for song in self.songs:
            if song.genre == genre: songs.append(song)
        return songs

    def play(self):
        for song in self.songs:
            song.play()     

    def addSong(self,song):
        self.songs.append(song)

    def deleteSong(self,song):
        self.songs.remove(song)