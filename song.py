class Song:
    """Class to represent a song
    Attributes:
        title (str)
        artist (Artist)
        duration (int)
    
    """
    def __init__(self, title, artist, duration=0): # duration default to zero
        """
        Song init method
        Args:
        :param title: Initialises the 'title' attribute
        :param artist: At Artist object representing the song's creator
        :param duration: Initial value for the 'duration' attribute.
                        Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

