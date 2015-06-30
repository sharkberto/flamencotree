# -*- coding: utf-8 -*-
import re
import codecs
#
#def organize_songs(text):
#

# splits data into albums
with codecs.open('artist_test.txt', encoding="latin-1") as raw:
    text = raw.read()
    chunks = text.split('''<p style="font-weight:bold;font-size:1.5em;text-align:center;">''')

    for i in range(len(chunks)):

        # separate album title from tracks and delete track list
        chunks[i] = chunks[i].split('''<p style="font:bold  .8em verdana;">''')
        chunks[i][0] = chunks[i][0].split('\n',1)[0]
        # now each chunk is length of tracks, [0] element has album info

        ## Insert code to make first element artist, second element album
        ## pass the artist/album extractor a chunk
        

    
         
    

##    # erase tags
##    for index in range(len(chunks)):
##            for index2 in range(len(chunks[1])):
##                    # Delete tags and new lines
##                    chunks[index][index2] = re.sub('<.*?>', '', chunks[index][index2])
##                    chunks[index][index2] = re.sub('"<p."', '', chunks[index][index2])
##                    chunks[index][index2] = re.sub('<p style="font:bold', '', chunks[index][index2])
##                    chunks[index][index2] = re.sub('\n', ' ', chunks[index][index2])
##    #return chunks
