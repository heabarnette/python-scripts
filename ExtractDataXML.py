#prompt for a URL, read the XML using urllib
#parse and extract the comment counts from the XML data
#compute the sum of the numbers in the file

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')

#print counts
line = 0
#counts = map(int, counts)
total = list()
for count in counts:
    num = count.text
    #print num
    num = int(num)
    total.append(num)
    line = line + 1


print "Count: ",line
print "Sum: ",sum(total) 
