# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:30:57 2020

@author: jayps
"""

scor = input("Enter Score: ")
score = float (scor)

if score > 1 or score < 0 :
    print("Range of score is from 0 to 1")

elif score >=0.9:
    print("A")
    
elif score >=0.8:
    print("B")
    
elif score >=0.7:
    print("C")
    
elif score >=0.6:
    print("D")

else :
    print("F")