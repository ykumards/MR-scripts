#!/usr/bin/env python
import sys
import string
import numpy

for line in sys.stdin:
    line = line.strip()
    
    # Initialize the counts of Java, hackathon, Chicago and Dec to 0
    # Since the reducer just adds the values per tag, these extra terms won't hurt
    search = ['Java', 'hackathon', 'Chicago', 'Dec']
    for term in search:
        print '%s\t%s' %(term, 0)
    # Split each line into Date, Time, Tag and Tweet
    words = line.split(',')
    date = words[0]
    month = date.split('-')[1]
    time = words[1]
    tag = words[2]
    tweet = ','.join(words[3:])
    if month == 'Dec':
        print '%s\t%s' %(month, 1)
    
    for word in tweet.split():
        # tab-delimited; the trivial word count is 1
        w = word.strip(string.punctuation)
        if w == 'hackathon' or w == 'Hackathon':
            print '%s\t%s' % ('hackathon', 1)
        if w == 'Chicago' or w == 'Java':
            print '%s\t%s' % (w, 1)

