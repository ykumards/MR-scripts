#!/usr/bin/env python

import re 
import sys

for line in sys.stdin:
    line = line.strip()
    date,time,name,tweet = line.split(',',3)
    words = re.findall(r"[\w']+", line)
    words = map(str.lower, words)
    leng = str(len(words))
    search = {'java': 0, 'hackathon': 0, 'chicago': 0, 'dec': 0}
    for word in words:
        if word in search:
            search[word] += 1

    #print "%s\t%s\t%s\t%s\t%s" %(date,time,name,tweet, leng)

    java_count = search['java']
    hack_count = search['hackathon']
    chicago_count = search['chicago']
    dec_count = search['dec']
    print "%d\t%d\t%d\t%d" %(java_count, hack_count, chicago_count, dec_count) 


