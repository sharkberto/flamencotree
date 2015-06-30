import re
from organizeraw import chunks

# match char-only string, no nums between a period and space, and tag '</p>'
artist_regex = re.compile('(?<=\W\s)(\D*?)(?=\<\/[p])') 
artist_regex_in_track = re.compile('(?<=\D[\)\.]\s)(\D*?)(?=<BR>)') # must have closing parentheses or period for backref
unclean_training_samples = []
clean_training_samples = []

#non-digits b/w non-alphanum and non-alphanum
song_title_regex = re.compile('([A-Z].*?)(?=<BR>)')

# ***** ARTIST EXTRACTION **** goes into position 0
for i in range(len(chunks)):
    artistSearchInHeader = re.search(artist_regex, chunks[i][0]) 
    if artistSearchInHeader == None:
        for j in range(len(chunks[i])):
            
            # existing name after ')' or '.' in song title?
            # e.g. Fandangos naturales. Ramon Moreno
            # e.g. El secreto de mi vida (fandangos) Juan Cantero
            # split artist name from track title
            artistSearchInTrack = re.search(artist_regex_in_track, chunks[i][j])   
            if artistSearchInTrack == None:
                chunks[i][j] = ['NA', chunks[i][j]]

                #
                # INSERT CODE TO HANDLE CASE FOR ARTIST = 'NA'
                #
                
            else:
                chunks[i][j] = [artistSearchInTrack.group(0), chunks[i][j]]

                
    if artistSearchInHeader != None:
        
        # save artist found in header until no other names found in track titles
        temp_artist_name = artistSearchInHeader.group(0)

        for j in range(len(chunks[i])):
            
            artistSearchInTrack = re.search(artist_regex_in_track, chunks[i][j])    
            
            if artistSearchInTrack == None:  
                
                chunks[i][j] = [temp_artist_name, chunks[i][j]]

            else:
                chunks[i][j] = [artistSearchInTrack.group(0), chunks[i][j]]
         

## **** SONG TITLE **** song goes into position 1, letras at position 2
                
for i in range(len(chunks)):
    for j in range(len(chunks[i])):
        songTitleSearch = re.search(song_title_regex, chunks[i][j][1])
        if songTitleSearch != None:
            chunks[i][j].insert(1, songTitleSearch.group(0))
        else:
            chunks[i][j].insert(1, 'NA')

## ***** PALO **** goes into position 2, letras go to position 3

palo_regex = re.compile('(?<=\()(.*?)(?=\))')

for i in range(len(chunks)):
    for j in range(len(chunks[i])):
        extracted_palo = re.search(palo_regex, chunks[i][j][2])
        if extracted_palo == None:      
            chunks[i][j].insert(2, 'NA')
            unclean_training_samples.append(chunks[i][j])       
        else:    
            chunks[i][j].insert(2, extracted_palo.group(0))
        
## **** VERSES **** verse count goes to position 3, letra goes into position 4

# Count number of verses in each letra, append to end of chunk[i][j], delete tags

for i in range(len(chunks)):
    for j in range(len(chunks[i])):
        chunks[i][j].insert(3,chunks[i][j][2].count('<P>'))

## ***** CLEAN OUT HTML *****
        
for i in range(len(chunks)):
    for j in range(len(chunks[i])):
        chunks[i][j] = re.sub('<.*?>', '', chunks[i][j][4])
        chunks[i][j] = re.sub('"<p."', '', chunks[i][j][4])
        chunks[i][j] = re.sub('<p style="font:bold', '', chunks[i][j][4])
        chunks[i][j] = re.sub('\n', ' ', chunks[i][j][4])

## SOME ISSUES ARE EXPECTED WITH THE EXTRACTION. DATA WILL HAVE TO BE CLEANED LATER

    
