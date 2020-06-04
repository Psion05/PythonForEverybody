# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#iteration is the number of times we have to dive in the link
lineno = int(input('Enter line no - '))
iteration = int(input('Enter iteration - '))

# int(lineno)
# int(iteration)
for num in range (0, iteration):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 1


    for tag in tags:
        #count is 1, if count goes above line no, we break out to outeloop
        #since we must've found the name
        if count > lineno: break

        #until we get to the line no, increase count by 1 and continue loop
        if count != lineno:
            count += 1
            continue

        #when correctly landed, assign value of name to name var by .contents[]
        #and increment count by 1 so we break out to outerloop and start next
        #iteration
        else :
            url = (tag.get('href', None))
            name = tag.contents[0]
            #print('Contents:', tag.contents[0])
            count = count + 1

            # http://py4e-data.dr-chuck.net/known_by_Fikret.html - sample 3-4
            # http://py4e-data.dr-chuck.net/known_by_Ralph.html - actual  18-7
print(name)
