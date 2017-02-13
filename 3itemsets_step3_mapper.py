#!/usr/bin/env python

import sys
import re

final_list_three = []
final_list_two = []

f = open('candidates', 'r')

itemset_3 = []
for line in f.readlines():
	line = line.strip()
	itemset_3.append(re.split(r'\t+',line))


# input comes from STDIN (standard input)
for line in sys.stdin.readlines():
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        #words = re.findall(r"[\'A-Za-z]+", line)
        words = line.split(' ')

	for each_itemset in itemset_3:
		#for word in words:
			#print(each_itemset[0])
		val = set(each_itemset) < set(words)
			#print(val)
		if(val==True):
			#print(each_itemset)
			print('%s,%s,%s\t%s' % (each_itemset[0],each_itemset[1],each_itemset[2], 1))
	
	#break
	
			#if(val == True):
				#print("\n")
			#	print(each_itemset)
				#print('%s,%s,%s\t%s' % (each_itemset[0],each_itemset[1],each_itemset[2], 1))	
