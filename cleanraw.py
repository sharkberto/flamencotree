# -*- coding: utf-8 -*-
import re
from organizeraw import chunks

# match char-only string, no nums between a period and space, and tag '</p>'
artist_regex = re.compile('(?<=\W\s)(\D*?)(?=\<\/p>)') 
artist_regex_in_track = re.compile('(?<=\D[\)\.]\s)(\D*?)(?=\/p>)')
#non-digits b/w non-alphanum and non-alphanum
song_title_regex = re.compile('([A-Z].*?)()(?=[\.\(\<])')#old= ('([A-Z].*?)(?=\W\s)
palo_regex = re.compile('(?<=\()(.*?)(?=\))')

lyrics = []
palos = []
verse_counts = []
artists = []
song_titles = []



# ***** ARTIST EXTRACTION **** the song title and artist likely in [i][0]
## each element [i][j] has a song 
for i in range(len(chunks)):
    artistSearchInHeader = re.search(artist_regex, chunks[i][0]) 
    if artistSearchInHeader == None:
        for j in range(1,len(chunks[i])):
            
            # existing name after ')' or '.' in song title?
            # e.g. Fandangos naturales. Ramon Moreno
            # e.g. El secreto de mi vida (fandangos) Juan Cantero
            # split artist name from track title
            artistSearchInTrack = re.search(artist_regex_in_track, chunks[i][j])   
            if artistSearchInTrack == None:
                artists.append('NA')
                
            else:
                artists.append(artistSearchInTrack.group(0))

                
    if artistSearchInHeader != None:
        
        # save artist found in header until no other names found in track titles
        temp_artist_name = artistSearchInHeader.group(0)

        for j in range(1,len(chunks[i])):
            
            artistSearchInTrack = re.search(artist_regex_in_track, chunks[i][j])    
            
            if artistSearchInTrack == None:  
                
                artists.append(temp_artist_name)

            else:
                artists.append(artistSearchInTrack.group(0))
         

## **** SONG TITLE **** 
                
for i in range(len(chunks)):
    for j in range(1,len(chunks[i])):
        songTitleSearch = re.search(song_title_regex, chunks[i][j])
        if songTitleSearch != None:
            song_titles.append(songTitleSearch.group(0))
        else:
            song_titles.append('NA')

## ***** PALO *****

for i in range(len(chunks)):
    for j in range(1,len(chunks[i])):
        extracted_palo = re.search(palo_regex, chunks[i][j])
        if extracted_palo == None:      
            palos.append('NA')       
        else:    
            palos.append(extracted_palo.group(0))
        
## **** VERSES **** verse count goes to position 3, letra goes into position 4

# Count number of verses in each letra, append to end of chunk[i][j], delete tags

for i in range(len(chunks)):
    for j in range(1,len(chunks[i])):
        
        verse_counts.append(chunks[i][j].count('<P>'))

## ***** LYRICS ***** for each chunks except the header...


## ***** CLEAN OUT HTML FROM LYRICS *****

song_header_regex = re.compile('^.*?<\/p>')
for i in range(len(chunks)):
    for j in range(1,len(chunks[i])):
        chunks[i][j] = re.sub('\n', ' ', chunks[i][j])
        chunks[i][j] = re.sub(song_header_regex, '', chunks[i][j])
        chunks[i][j] = re.sub('<.*?>', '', chunks[i][j])
        chunks[i][j] = re.sub('\r', '', chunks[i][j])
##        chunks[i][j] = re.sub('"<p."', '', chunks[i][j])
##        chunks[i][j] = re.sub('<p style="font:bold', '', chunks[i][j])
        
        lyrics.append(chunks[i][j])
        
        
## ***** CLEAN OUT HTML FROM ARTISTS AND SEND FEATURES TO FILES*****
with open('lyrics.txt', 'w+') as lyrics_doc:
    with open('palos.txt', 'w+') as palos_doc:
        with open('verse_counts.txt', 'w+') as verse_counts_doc:
            with open('testlyrics.txt', 'w+') as testlyrics:
                with open('testpalos.txt', 'w+') as testpalos:
                    with open('testverse_counts.txt', 'w+') as testverse_counts:
                        with open('song_titles.txt', 'w+') as songs:
                            for i in range(len(lyrics)):
                                lyrics[i] = re.sub('\r\n', '', lyrics[i])
                                songs.write(song_titles[i].encode('utf-8') + '\n')
                                #if the palo is valid, we can use the lyrics in training
    ##                            if palos[i][0].islower():
                                lyrics_doc.write(lyrics[i].encode('utf-8') + '\n')
                                palos_doc.write(palos[i].encode('utf-8') + '\n')
                                verse_counts_doc.write(str(verse_counts[i]) + '\n')
    ##                            else:
    ##                                testlyrics.write(lyrics[i].encode('utf-8') + '\n')
    ##                                testpalos.write(palos[i].encode('utf-8') + '\n')
    ##                                testverse_counts.write(str(verse_counts[i]) + '\n')
##
##
## SOME ISSUES ARE EXPECTED WITH THE EXTRACTION. DATA WILL HAVE TO BE CLEANED AND
## DATA ZIPPED TOGETHER IN COMPREHENSIVE FORMAT                           

## to create dictionary of items for json dict to pass to Dictvectorizer in scikitleanr
## palo_song_dict = dict(zip(palos,song_titles)
## 
    
