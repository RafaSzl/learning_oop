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
        :param position: If specified, the song will be added to that position in the track list- inserting
        it between other songs if necessary.
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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)  # creating an object
            elif new_artist.name != artist_field:
                # We are just read details for a new artist
                # store current album in currents artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)  # here we add new_artist to artist_list
                new_artist = Artist(artist_field)  # initialize another artist?
                new_album = None  # setting album to none to add it from a begining

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)  # creating an object
            elif new_album.name != album_field:
                # We are just read a new album for the current artist
                # store current album in the artist's collection then create new album obcject
                new_artist.add_album(new_album)  # here may be error
                new_album = Album(album_field, year_field, new_artist)

            # create new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After read the last line of the text file, we will have an artist and
        # album that haven't been store - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file
    """
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
