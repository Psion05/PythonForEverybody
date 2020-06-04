
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

counts = dict()
#empty dictionary

for line in handle:
    if not line.startswith('From:') : continue
    #if line not start with 'From:', we go to next iteration

    words = line.split()
    # split() creates a list of words in line

    counts[words[1]] = counts.get(words[1], 0) + 1
    #if 2nd word(the one we want) is not in count, then add word to count using .get method (read more about it)


# print(counts)
bigCount = None
bigName = None


for name, count in counts.items():
#name and count are variables for 'key' and 'value' in dict()
    if bigCount is None or  count > bigCount:
    #bigCount is None is applied only on 1st integration
    #rest is code logic to assign bigCount and bigName the highest 'value' and it's respective 'key'    
        bigCount = count
        bigName = name

print(bigName,bigCount)
