#any-char check 

import re 

with open("sample.txt") as hand:
    for line in hand:
        line= line.rstrip()
        if re.search("^h.",line):
            print (line)