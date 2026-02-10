# Create a MusicPlayer class and subclass Spotify to override play method.
class MusicPlayer:
    def __init__(self, song):
        self.song = song
    def play(self):
        print(f"Playing {self.song} on generic music player")
class Spotify(MusicPlayer):
    def play(self):
        print(f"Playing {self.song} on Spotify with premium features")
player1 = MusicPlayer("Shape of You")
player1.play() 
player2 = Spotify("Blinding Lights")
player2.play()  
