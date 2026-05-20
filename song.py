class Song: 
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration  # duration in seconds

    def __str__(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"'{self.title}' by {self.artist} from the album '{self.album}' - {minutes}:{seconds:02d} minutes"