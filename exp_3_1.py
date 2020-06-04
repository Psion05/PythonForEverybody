# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hrs = input ("Enter Hours: ")
hours = float (hrs)

rte = input ("Enter rate of pay: ")
rate = float(rte)

pay = hours * rate
newrate = rate * 1.5


if hours > 40:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * newrate)
    print(pay)

else:
    print(pay)
    
    