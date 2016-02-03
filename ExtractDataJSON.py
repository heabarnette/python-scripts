#prompt for a url, read json data using urllib
#parse and extract comment counts, compute sum

import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)

line = 0
total = list()
for each in info["comments"]:
    num = each["count"]
    num = int(num)
    total.append(num)
    line = line + 1

print "Count: ",line
print "Sum: ",sum(total) 
