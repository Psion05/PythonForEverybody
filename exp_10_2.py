# 10.2 Write a program to read through the mbox-short.txt and figure out the dicntribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# >>>From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008<<<
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dicn = dict()

for line in handle:
    if not line.startswith('From ') : continue


    line = line.rstrip()
    pos = line.find(":")
    line = line[pos-2:pos]
    # code to find postion of time and slice out only the time
    dicn[line] = dicn.get(line, 0) + 1
    #.get() method of dict where if  current line present in dict, increment its value by 1
    #if not, then add it and give default value of zero, and add one to zero
lst = list()

for k,v in list(dicn.items()):
#typecast dictionary.item as list, and then add tuples values to empty list
    lst.append((k,v))


lst.sort()

for k,v in lst:
#print out values with their keys from lst
    print(k,v)
