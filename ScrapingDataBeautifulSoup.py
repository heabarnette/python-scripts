#find all span tags, pull (convert to int) and sum numbers
import urllib

from BeautifulSoup import *
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
count = 0
total = list()
for tag in tags:
    num = tag.contents[0]
    comments = int(num)
    total.append(comments)
    count = count + 1
print "Count ",count
print "Sum ",sum(total) 