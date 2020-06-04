# Dictionaries Chapter
# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#
# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn't matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fname = input("Enter file name:")

if len(fname) < 1 : fname = 'words.txt'

fhand = open(fname)
compendium = dict()

for line in fhand:
    words = line.split()
    for element in words:
        compendium[element] = 'yes'

print(compendium)
