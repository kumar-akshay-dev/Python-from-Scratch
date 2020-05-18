# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:24:41 2020

@author: Kumar
Difference between match and search function :
match checks for a match only at the beginning of the string,
while search checks for a match anywhere in the string
"""


import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")


