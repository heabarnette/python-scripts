#who has sent most mail 

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#text = handle.read()
email = 0
counts = dict()

#look for 'From' lines
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    if line.startswith('From:') :continue
    words=line.split()
# take second word of line for key
    email = words[1]
    #print email
#create dictionary, count names
    counts[email] = counts.get(email,0) + 1
    #print counts
#max loop  
bigcount = None
bigemail = None
for email,count in counts.items():
    if bigcount == None or count > bigcount:
        bigemail = email
        bigcount = count
print bigemail, bigcount