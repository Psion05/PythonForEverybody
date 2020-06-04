#  In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers. 
# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#  looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers. 

import re


fname = input("enter file name:")
if len(fname) < 1 : fname = 'sample.txt'
elif len(fname) >= 1 : fname = 'actual.txt'

handle = open(fname)

sum = 0

for line in handle:
    line = line.rstrip()
    match = re.findall('([\d]+)',line)      #extracting only digits[(\d)+] using re.findall (note:this function returns a list of string type)
    if len(match) > 0:                      #if match has more than one unit of data, i.e it is not empty, then
        for i in range (0, len(match)):     # iterate through the list and in next line type cast them into integersm, then add to  sum.
            digit = int(match[i])
            sum = sum + digit

print(sum)
            
    
       
        
        
    
   

    
    
    
    
 
