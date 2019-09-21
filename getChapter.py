import sys
import random

scripture = sys.argv[1]
scriptures = ['bom', 'dnc', 'nt', 'ot']
chapters = []
if scripture in scriptures:
    with open('{}.txt'.format(scripture)) as inFile:
        for line in inFile:
            chapters.append(line)


    print(chapters.pop(random.randint(1,len(chapters))))

    with open('{}.txt'.format(scripture), 'w') as outFile:
        outFile.writelines(chapters)

else:
    print("Options are: bom, dnc, nt, ot")
