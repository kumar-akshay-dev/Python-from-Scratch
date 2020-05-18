# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:16:17 2020

@author: kumar

match function:This function attempts to match RE pattern to string
Syntax:
    re.match(pattern, string, flags=0)
"""

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line)

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group() : ", matchObj.group(1))
    print ("matchObj.group() : ", matchObj.group(2))
else:
   print ("No match!!")



