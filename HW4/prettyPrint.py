import os
import sys

search_list = ['Chicago', 'Dec', 'Java', 'hackathon']

fo = open("output.txt", "rw+")

for name in search_list:
    filename = name + '/part-r-00000'
    with open(filename) as f:
        line = f.readlines()
        num = int(line[0].strip())
        s =  "%s\t%d" %(name, num)
        print s
        fo.write(s)
        fo.write("\n")
    f.close()
fo.close()

    
