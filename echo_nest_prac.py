from pyechonest import config
config.ECHO_NEST_API_KEY="AFGRWXTC8P8BCOGJM"
from pyechonest import artist
from pyechonest import song
from artist_extract import chunks


def getSongsByArtist(name):
    a = artist.Artist(name)
    with open('API_results.py', 'w+') as f:
        if a:
            print a.get_songs()
            f.seek(0)
            f.write(str(a.get_songs()))
            f.close()
            #should return song names

#Takes a list of artists and processes desired data
for i in range(len(chunks)):
    flamenco_artist = chunks[i][0][0]

    if flamenco_artist != 'NA':
        valid_utf8 = True
        try:
            getSongsByArtist(flamenco_artist)
        except UnicodeDecodeError:
            valid_utf8 = False


                


