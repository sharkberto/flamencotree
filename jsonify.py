#-*- coding: utf-8 -*-
import json
import itertools

data = {} # the X training data
palos = [] # the Y labels
song_titles = []
lyrics = []
num_verses = []

with open('true_palos.txt', 'r') as palos_doc:
    with open('song_titles.txt', 'r') as titles:
        with open('lyrics.txt', 'r') as lyrics_doc:
            with open('verse_counts.txt', 'r') as verse_counts:
            
                for palo in palos_doc:
                    palo = palo.rstrip('\n')
                    palos.append(palo)
                    for title in titles:
                        title = title.rstrip('\n')
                        song_titles.append(title)
                        for lyric in lyrics_doc:
                                lyric = lyric.rstrip('\n')
                                lyrics.append(lyric)
                                for num_verse in verse_counts:
                                    num_verse = num_verse.rstrip('\n')
                                    num_verses.append(num_verse)

                   
# This dictionary is to allow for feature mapping for scikitlearn's dictvectorizer
# for each palo, make a list, if palo, seen before add to list of values for that palo

#ideally:
##{
##  "title" : "1","2","3"
##  "lyrics" : "sdf","tre","wer"
##  "verses" : "a", "b", "c"


def insertIntoDict(name,title,lyr,num,aDict):
    if not name in aDict:
        aDict[name] = [({'title' : title},{'lyrics' : lyr},{'verses' : num})]
    else:
        aDict[name].append(({'title' : title},{'lyrics' : lyr},{'verses' : num}))


for i in range(len(palos)):
    insertIntoDict(palos[i],song_titles[i],lyrics[i],num_verses[i], data)

with open('flamencodict.json', 'w') as out:
    json.dump(data, out, sort_keys=True,
                  indent=4, separators=(',', ': '))
#, sort_keys = True, indent =4, ensure_ascii=False)
##for i in range(len(palos)):
##    if data[palos[i]] == True:
##        data[palos[i].insert([{'title' : song_titles[i]},
##                {'lyrics' : lyrics[i]},
##                {'verses' : num_verses[i]}
##                 ]})
##        data.update({palos[i] : [
##                {'title' : [song_titles[i]]},
##                {'lyrics' : [lyrics[i]]},
##                {'verses' : [num_verses[i]]}
##                 ]})



