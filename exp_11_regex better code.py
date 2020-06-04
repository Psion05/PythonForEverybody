# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:20:28 2020

@author: Psion05
"""


# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the add of the numbers. 
# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#  looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and addming up the integers. 

import re


fname = input("enter file name:")
if len(fname) < 1 : fname = 'sample.txt'
elif len(fname) >= 1 : fname = 'actual.txt'

handle = open(fname)

add = 0

for line in handle:
    line = line.rstrip()
    match = re.findall('([\d]+)',line)      #extracting only digits[(\d)+] using re.findall (note:this function returns a list of string type)
    listadd = sum(list(map(int,match)))     #here, we map all elements of list 'match' to int type, then we put all of them to a list, and then we use
                                            # built-in function sum to addition all elements of that list and assign the summed up value to add variable
    add = add + listadd

print(add)
            
    