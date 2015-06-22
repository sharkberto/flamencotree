import re, json
from organize_canteytoque import *

# open flamenco file
with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawtitleletras.txt') as doc:
    text = doc.read()

# return song data in an array of text chunks
chunks = organize_songs(text)



with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawletras.json', 'w+') as samples:

    # regex to get the palo name out of parens in the song title
    palo_regex = re.compile('(?<=\()(.*?)(?=\))') 

    for index in range(len(chunks)):

        # getting palo name from the title
        match = re.search(palo_regex, chunks[index][0]) 

        if re.search(palo_regex, chunks[index][0]) != None: 

            #insert in first position
                #rename cleaned up chunks as training set
            chunks[index].insert(0, match.group(0)) 
    
        else: chunks[index].insert(0, 'NA') 

        #if palo has 'NA', add to separate list 'unclean_train_set' and delete element from chunks


    #creating dictionary structure
    flamenco_dict = {}




    #initializing the dictionaries and writing to files
    with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\rawletras_labels.json', 'w+') as sample_labels:

        for idx in range(len(chunks)):
            # create the dictionary element to add to the main dictionary
            flamenco_nextdict = {chunks[idx][1]:chunks[idx][2]}
            
            # add each song
            flamenco_dict.update({chunks[idx][0] : flamenco_nextdict})
            
            # write the letras to the first file
            samples.write(chunks[idx][2] + '\n')
            
            # write the letra labels to the second file
            sample_labels.write(chunks[idx][0] + '\n') 




    # compile dictionaries into json format...may be useful later
    flamenco_dict_json = json.dumps(flamenco_dict, sort_keys=False, indent=4, separators=(',', ': '))

        
    




# validate palos to ensure no extraneous info and harmonize naming    
##with open ('C:\Users\Alex\Documents\\flamenco_data\palos_singular.txt','r+') as palos_singular:
##    palos = [line.strip('\n') for line in palos_singular]
##    palos = [line.lower() for line in palos]



    



    
    
    
