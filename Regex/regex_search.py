# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:19:11 2020

@author: Kumar

search Function:This function searches for first occurrence of RE pattern 
within string with optional flags.
Syntax:
re.search(pattern, string, flags=0)
"""

#using search pattern to check for a pattern present 
import re
match1=re.search('apple', 'i love apples')
print(match1) 
match2=re.search('none', 'i love apples')
print(match2)  

print(match1.re.pattern) #to get the searched pattern
print(match1.string)   # to get the searched string
print(match1.start())  # to get the start position
print(match1.end())    # to get the end position


line = "Cats are smarter than dogs and cow"
searchObj = re.search( r'(.*) are (.*?) .*', line)

"""
group(num=0) : This method returns entire match (or specific subgroup num)
groups() : This method returns all matching subgroups in a tuple
 (empty if there weren't any)
"""
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*) and (.*)', line)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group() : ", searchObj.group(1))
   print ("searchObj.group() : ", searchObj.group(2))
   print ("searchObj.group() : ", searchObj.group(3))
else:
   print ("Nothing found!!")
