#!/usr/bin/env python

from operator import itemgetter
import sys

current_link = None
current_value = 0
link = None
source = None
outlinks = []
current_outlinks = []

for line in sys.stdin:
    link, values = line.strip().split('\t', 1)
    # There were two types of values from mapper
    # one was , separated and other space separated
    comma_split = values.split(',')
    
    if len(comma_split) < 2:
        outlinks = values.split()
        value = 0
    else:
        value = comma_split[0]

    #convert outlink_value (currently a string) to float
    try:
        value = float(value)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    #this IF-switch only works because Hadoop sorts map output
    #by key (here: word) before it is passed to the reducer
    if current_link == link:
        current_value += value
        current_outlinks = outlinks
    else:
        # If we hit a new link, print the old
        if current_link:
            # write result to STDOUT
            print '%s %s %s' %(current_link, " ".join(current_outlinks), current_value)
        current_value = value
        current_link = link
        current_outlinks = outlinks

# do not forget to output the last word if needed!
if current_link == link:
    print '%s %s %s' % (current_link, " ".join(current_outlinks) ,current_value)
