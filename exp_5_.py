# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:58:55 2020

@author: jayps
"""

largest = None
smallest = None

while True:
    try:
        strint = input("Gimme dem integers:")
        if strint == 'done':
            break
        else:
            num = int (strint)
            #print(num)
            
            if largest is None or num > largest:
                
                largest = num
                continue
            
            elif smallest is None or num < smallest:
                smallest = num
            
            
    except:
        print("Invalid input")
        continue



print("Maximum is",largest)
print("Minimum is",smallest)
    
    
    
    
        
            
            
            
        
        
        
    
        
    
    