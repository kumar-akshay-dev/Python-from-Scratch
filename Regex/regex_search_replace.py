# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:29:04 2020

@author: Kumar
Search and Replace:This method replaces all occurrences of the RE pattern 
in string with repl, substituting all occurrences unless max provided. 
This method returns modified string.
"""

import re
phone = "2004-959-559 # This is Phone Number"

# remover comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything '-'
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)


