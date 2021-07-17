# from __future__ import print_function
# it allows to print in python 2 the things wrote in python 3

class Song:
    """Class to represent a song

    Attributes:
        title (str)
        duration (int)
    """

    def __init__(self, title, duration=0):  # duration default to zero

        # Below is the docstring for init method from line 12 to 19
        """Song init method

        Args:
        :param title: Initialises the 'title' attribute
        :param duration: Initial value for the 'duration' attribute.
                        Will default to zero if not specified
        """
        self.title = title
        self.duration = duration

    def get_title(self):  # GETTER FUNCTION - that its name
        return self.title

    name = property(get_title)  # on this line we allow this program to work even with title instead of name attribute


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of an album.
        year (int): The year album was released.
        If not specified the artist will default be tnamed "Various Artists".
        tracks (Lists[Song]): A list of the songs on the album.

        Methods:
            add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year

        self.tracks = []
        # Not every attribute needs to be a parameter of the init method. The parameters of the init
        # method are for things that differ between objects, and for some classes, certain attributes start off the same
        # for every object. Every Album object starts with an empty list for the tracks attribute, and there is no
        # reason for this to be configurable.

        # Keyword parameters like with artist=None are slightly different. They let you set a default value for
        # a parameter that is going to be the same for most objects of a given class, but not all of them.

    def add_song(self, song, position=None):  # position=None - add song to the end of a list
        """Adds a song to the track list

        Args:
        :param song: The title of a song to add.
        :param position: If specified, the song will be added to that position in the track list- inserting
        it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        :return:
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song)
            if position is None:
                self.tracks.append(song_found.name)
            else:
                print("Found song " + song)
                self.tracks.insert(position, song_found)  # doda piosenki na koncu listy dzieki insert i position=None


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

    def add_song(self, name, year, title):
        """Add new song to the collection of albums
        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:  # if it does not exist in our albums attribute
            print(name + " not found")
            album_found = Album(name, year)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


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
                new_artist = Artist(artist_field)  # creating an instance of Artist class (creating object)
                artist_list.append(new_artist)  # we add artist to list bcs now we can check if artist is in a list and eventually move forward
            elif new_artist.name != artist_field:  # zostanie wykonane jezeli bedzie spelniony ten warunek, jezeli nie to idzie dalej i pomija te czesc
                # We are just read details for a new artist
                # retrieve the artist object if there is one, otherwise creaste a new artist obj and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:  # this is necessary due to how find_object func is written
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field)  # creating an object
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We are just read a new album for the current artist
                # retrieve the album object if there is one, otherwise creaste a new album obj and add it to the artist collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None: # this is necessary due to how find_object func is written
                    new_album = Album(album_field, year_field)
                    new_artist.add_album(new_album)

            # create new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

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
