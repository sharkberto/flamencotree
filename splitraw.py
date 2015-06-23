import re, json
from organize_canteytoque import *

#
# open flamenco file
with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawtitleletras.txt') as doc:
    text = doc.read()
#
# Pre-processing
#

song_chunks = organize_songs(text)


with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawletras.json', 'w+') as samples:
    palo_regex = re.compile('(?<=\()(.*?)(?=\))')
    unclean_training_samples = []
    clean_training_samples = []
    for index in range(len(song_chunks)):
        extracted_palo = re.search(palo_regex, song_chunks[index][0])
        if extracted_palo == None:
            song_chunks[index].insert(0, 'NA')
            unclean_training_samples.append(song_chunks[index]) ## Insert palo name in first position      
            # del song_chunks[index], recode so the unwanted elements can be taken at end, by keeping
            # list of their indices
            # for itemnum in NAitemlist: song_chunks.pop(itemnum)
        else:
            song_chunks[index].insert(0, extracted_palo.group(0))
    # remove the 'NA' palo samples from the song_chunks set
        
        
            

# If palo has 'NA', add to other list and delete element from song_chunks
#



##
# Create dictionary structure
##

    flamenco_dict = {}


    with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawletras_labels.json', 'w+') as sample_labels:

        for idx in range(len(song_chunks)):
            # create the dictionary element to add to the main dictionary
            flamenco_nextdict = {song_chunks[idx][1]:song_chunks[idx][2]}
            
            # add each song
            flamenco_dict.update({song_chunks[idx][0] : flamenco_nextdict})
            
            # write the letras to the first file
            samples.write(song_chunks[idx][2] + '\n')
            
            # write the letra labels to the second file
            sample_labels.write(song_chunks[idx][0] + '\n') 




    # compile dictionaries into json format...may be useful later
    flamenco_dict_json = json.dumps(flamenco_dict, sort_keys=False, indent=4, separators=(',', ': '))

        
    




# validate palos to ensure no extraneous info and harmonize naming    
##with open ('C:\Users\Alex\Documents\\flamenco_data\palos_singular.txt','r+') as palos_singular:
##    palos = [line.strip('\n') for line in palos_singular]
##    palos = [line.lower() for line in palos]



    



    
    
    
