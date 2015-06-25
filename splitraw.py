import re, json
from organize_canteytoque import *

# Open flamenco file for pre-processing
with open('rawtitleletras.txt') as doc:
    text = doc.read()

    # Separate songs, delete HTML tags and line breaks
    song_chunks = organize_songs(text)
    unclean_training_samples = []

    # Regex for grabbing the 'palo' aka song style from ( ) in title
    palo_regex = re.compile('(?<=\()(.*?)(?=\))')
    
    # Put palo name in first position or if none insert 'NA' in first position
    for index in range(len(song_chunks)):
        extracted_palo = re.search(palo_regex, song_chunks[index][0])
        if extracted_palo == None:      
            song_chunks[index].insert(0, 'NA')
            unclean_training_samples.append(song_chunks[index])       
        else: 
            
            song_chunks[index].insert(0, extracted_palo.group(0))

    # Remove the 'NA' palo samples from the sample set  
    def checkforNA(x): return x[0] != 'NA'

    song_chunks = filter(checkforNA, song_chunks)

    # Remove the album metadata from the sample set
    def checkforAlbum(x):
        album_info_regex = re.compile('\s\d')
        anyAlbumInfo = re.search(album_info_regex, x[2])
        return anyAlbumInfo == None

    
    song_chunks = filter(checkforAlbum, song_chunks)  

    # Song data is ready to export
    with open('samples.txt', 'w+') as samples:
        with open('sample_labels.txt', 'w+') as sample_labels:
        
            for idx in range(len(song_chunks)):

                # Write the sample to the first file
                samples.write(song_chunks[idx][2] + '\n')
            
                # write the letra labels to the second file
                sample_labels.write(song_chunks[idx][0] + '\n') 






    



    
    
    
