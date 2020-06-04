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
lst = list()

for line in handle:
    if not line.startswith('From ') : continue


    line = line.rstrip()
    words = line.split()
    #splits line in list of words, note that time 09:14:16 from question is one word.
    words = words[5]
    #assigns the time value of words to words

    hr = words.split(':')
    #splits time using delimiter colon so now its a list of 09,14,16
    hr = hr[0]
    #finally we capture the hour, (what we need for the answer)

    dicn[hr] = dicn.get(hr, 0) + 1    #increase count for each hour
    
    #.get() method of dict where if  current line present in dict, increment its value by 1
    #if not, then add it and give default value of zero, and add one to zero


# print(dicn)
 # was used for testing


for k,v in dicn.items():
    lst.append((k,v))


lst.sort()

for k,v in lst:
#print out values with their keys from lst
    print(k,v)
