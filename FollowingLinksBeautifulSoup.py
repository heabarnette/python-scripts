#find all anchor tags, find link at position, 
#follow link and repeat x times, print last name
import urllib
import json
import ssl

from BeautifulSoup import *
url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position) - 1

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
html = uh.read()

for x in range(0, count): 
    soup = BeautifulSoup(html)
    tags = soup('a')
    print "Retrieving: ",url
    url = tags[position].get('href',None)  
    uh = urllib.urlopen(url, context=scontext)
    html = uh.read()
            
print "Last Url: ",url
