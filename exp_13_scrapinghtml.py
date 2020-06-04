# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
#initialize a list
lis = list()

for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)

    '''
    example output of tag and content - TAG: <span class="comments">79</span>
                                        Contents: 79
    we are interested in content which we access using tag.contents[0]

    '''
    #print('Contents:', tag.contents[0])

    #append value of content section to list, list type we get will be string
    lis.append(tag.contents[0])


#using map function, type cast int iteratively through the list, and then
#sum everything up using builtin sum() functuon

listadd = sum(map(int,lis))

print(listadd)
