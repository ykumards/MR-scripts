#!/usr/bin/env python
"""
Mapper to perform Page Rank
Input: of the form 'A C D val', which means C and D are outlinks from A 
Output: Separate line for each outlink and the value is PR(A)/total outlinks from A. Also store the source for each outlink
since we have to remap it during the output.
Also print another line that has the original links A C D, in that order

NOTES: Choosing the output format was tricky. The reducer had
to deal with two kinds of input, 'A C F' and 'C value'. To ensure that the 'C value' type inputs are given to the reducer first, print values first, then source 

"""
import sys

for line in sys.stdin:
    words = line.strip().split()
    source = words[0] # First link is the source
    total_outlinks = len(words) - 2 # We need the number of outlinks to calculate PR
    link_value = float(words[-1])/total_outlinks 
    # Loop through each outlink to print out the value
    for i in xrange(1, len(words)-1):
        link = words[i];
        if link:
            print '%s\t%s,%s' % (link, link_value, source)
    print '%s\t%s' %(source, " ".join(words[1:-1]))
