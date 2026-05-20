class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        """Add a song to the playlist."""
        self.songs.append(song)

    def remove_song(self, song):
        """Remove a song from the playlist."""
        if song in self.songs:
            self.songs.remove(song)

    def get_songs(self):
        """Return the list of songs in the playlist."""
        return self.songs

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self.songs)}"