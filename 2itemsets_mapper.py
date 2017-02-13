#!/usr/bin/env python

import sys
import re

final_list = []
# input comes from STDIN (standard input)
for line in sys.stdin.readlines():
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        #words = re.findall(r"[\'A-Za-z]+", line)
        words = line.split(' ')
        # increase counters
        for i in range(0,len(words)-1):
		for j in range(i+1,len(words)):
                	# write the results to STDOUT (standard output);
        	        # what we output here will be the input for the
	                # Reduce step, i.e. the input for reducer.py
                	#
                	# tab-delimited; the trivial word count is 1
	                print('%s,%s\t%s' % (words[i],words[j], 1))
	
