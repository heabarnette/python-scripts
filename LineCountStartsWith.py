# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
lst = list ()
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From') :continue
    #if line.startswith('From:') :continue
    words=line.split()
    email=words[1]
    print email
    count = count + 1
print "There were", count, "lines in the file with From as the first word"