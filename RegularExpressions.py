import re
#read the file
handle = open('regex_sum_198891.txt')
#find integers
#sum integers
numlist = list()
#count = 0
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    #print stuff
    if len(stuff) <1 : continue
    #print stuff
    num = map(int, stuff)
    #print num
    subtotal = sum(num)
    numlist.append(subtotal)
#print numlist
total = sum(numlist)
print total