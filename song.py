class Song:
    """Class to represent a song

    Attributes:
        title (str)
        artist (Artist)
        duration (int)
    
    """

    def __init__(self, title, artist, duration=0):  # duration default to zero

        # Below is the docstring for init method from line 12 to 19
        """Song init method

        Args:
        :param title: Initialises the 'title' attribute
        :param artist: At Artist object representing the song's creator
        :param duration: Initial value for the 'duration' attribute.
                        Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of an album
        year (int): The year album was released
        artist (Artist): The artist responsible for the album.
        If not specified the artist will default be tnamed "Various Artists".
        tracks (Lists[Song]): A list of the songs on the album.

        Methods:
            add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year

        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
        :param song: A song to add
        :param position: If specified, the song will be added to that position in the track list- inserting it betweend other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        :return:
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            tHE List includes only those albums in this collection, it is
            not an exhastive list of the artist's published albums.

    Methods:
        add_album: Use add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add new album to the list.

        :param album: Album object to add to the list.
            If the album is already present, it will not be added again (although this is yet to implemented)

        """
        self.albums.append(album)

