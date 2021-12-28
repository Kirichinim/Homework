inFile = open('OTRIVOK IS PIESI.txt', 'r', encoding="utf-8"
              )
DICT ={}
G = 1
for line in inFile:
    O = line.split()
    DICT[O[0].strip('. ')] = DICT.get(O[0].strip('. '), '') + str(G) + ') ' + ' '.join(O[1:]) + '\n'
    G += 1
for key,value in DICT.items(): print(key, ':\n', value, sep='')
inFile.close()
