# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hrs = input ("Enter Hours: ")
hours = float (hrs)

rte = input ("Enter rate of pay: ")
rate = float(rte)


def computepay(hours,rate):
    
    
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
        
        return pay
    

    else:
        pay = hours * rate
        return pay
    
    
pay = computepay(hours, rate)

print (pay)