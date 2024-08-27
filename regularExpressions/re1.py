#a way to see if strings of text match or dont match 

import re 
with open("sample.txt") as hand :
    for line in hand :
        line=line.rstrip()
        if re.search("^From:",line):
            print (line)