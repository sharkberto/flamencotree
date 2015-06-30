import re
from organizeraw import chunks

# match char-only string, no nums between a period and space, and tag '</p>'
artist_regex = re.compile('(?<=\W\s)(\D*?)(?=\<\/[p])') 
artist_regex_in_track = re.compile('(?<=\D[\)\.]\s)(\D*?)(?=<BR>)') # must have closing parentheses or period for backref
#non-digits b/w non-alphanum and non-alphanum
song_title_regex = re.compile('([A-Z].*?)(?=<BR>)')
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


## ***** CLEAN OUT HTML *****

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
        




        
## lyrics are everything after the closing </p> tag
## SOME ISSUES ARE EXPECTED WITH THE EXTRACTION. DATA WILL HAVE TO BE CLEANED LATER

    
