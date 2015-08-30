import re
from collections import Counter
from pprint import pprint

#open palos_singular
with open ('C:\Users\Alex\Documents\flamenco_data\palos_singular.txt','r+') as palos_singular:
    palos = [line.strip('\n') for line in palos_singular]
    palos = [line.lower() for line in palos]

#open canteytoquetracks
with open ('canteytoquetracks.txt', 'r+') as canteytoquetracks:
    tracks = [line.strip('\n') for line in canteytoquetracks]
    tracks = [line.lower() for line in tracks]

palocounter = Counter()
palocheck = bool
#for each song in canteytoquetracks, find the palos that are included
for line in tracks:
    for palo in palos:
            if palo in line:
                palocounter[palo] += 1
                palocheck = True
                if palocheck == False:
                    print line
            #check if track had no palo
            
#if palos_singular in canteytoquetracks, dictionary[palos_singular : value + 1]

print palocounter.values()
#make a freq dist of the items in dictionary
