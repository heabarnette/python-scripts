# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        count = count + 1
        sppos = line.find(' ')
        val = line[sppos:]
        val = val.rstrip()
        val = float(val)
        sum = sum + val
   
print "Average spam confidence:",sum/count