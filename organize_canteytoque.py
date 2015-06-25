import re

def organize_songs(text):
    chunks = text.split('''.8em verdana;">''')
    for index in range(len(chunks)):
        chunks[index] = chunks[index].split('</p>',1)
    

    # erase tags
    for index in range(len(chunks)):
            for index2 in range(len(chunks[1])):
                    # Delete tags and new lines
                    chunks[index][index2] = re.sub('<.*?>', '', chunks[index][index2])
                    chunks[index][index2] = re.sub('"<p."', '', chunks[index][index2])
                    chunks[index][index2] = re.sub('<p style="font:bold', '', chunks[index][index2])
                    chunks[index][index2] = re.sub('\n', ' ', chunks[index][index2])
    return chunks
