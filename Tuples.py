name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#distribution for hour of the day

counts = dict()

#pull 'From ' lines
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') :continue
    if line.startswith('From:') :continue
    words = line.split()
#split hour using colon
    time = words[5]
    clock = time.split(':')
    hour = clock[0]
    #print hour 
#use hour for key
#create dictionary, count hours
    counts[hour] = counts.get(hour,0) + 1
    #print counts
#print counts, sorted by hour
lst = list()
for key,val in counts.items():
    lst.append((key,val))
lst.sort()
for key,val in lst:
    print key, val

