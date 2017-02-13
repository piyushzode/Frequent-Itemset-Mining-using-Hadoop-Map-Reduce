#!/usr/bin/env python

import sys
import re

final_list_three = []
final_list_two = []
# input comes from STDIN (standard input)
for line in sys.stdin.readlines():
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        #words = re.findall(r"[\'A-Za-z]+", line)
        #words = line.split('')
        words = re.split(r'\t+',line)
	if(len(words) == 3):
		final_list_three.append(words)
	elif(len(words) == 2):
		final_list_two.append(words)
	#list1 = [int(x) for x in words]
	#list1.sort()
	#sorted_li.append(list1)
        #final_list.append(words)
        # increase counters

#print(final_list)
#print("\n\nAfter sorting:\n")
#print(sorted_li)

#print(sorted(final_list, key=int))

#print(final_list_three)
#print("\n\nPrinting 2 size list")
#print(final_list_two)

for i in range(0,len(final_list_three)):
#	break
	B,C,A = final_list_three[i]
	    	
	#print(i,A,B,C)
	#break
	if([B,C] in final_list_two):
		print('%s,%s,%s\t%s' % (A,B,C, 1))
	
	#for j in range(i+1,len(sorted_li)):
	#	internal_A,C = sorted_li[j]
	#	tmp_li = []
	#	if(A == internal_A):
	#		#if([B,C] in final_list):
	#		tmp_li.append(A)
	#		tmp_li.append(B)
	#		tmp_li.append(C)
	#		list1 = [int(x) for x in tmp_li]
        #		list1.sort()
	#		print('%s,%s,%s\t%s' % (list1[1],list1[2],list1[0], 1))


#for i in range(0,len(final_list)-1):
#        for j in range(i+1,len(final_list)):
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1

 #               print('%s,%s\t%s' % (words[i],words[j], 1))

