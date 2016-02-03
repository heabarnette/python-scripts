# Use the file name romeo.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
lst= list()
for line in fh:
    line = line.rstrip()
    words = line.split() #split each line into a list of words
    for i in words:
        if i not in lst: 
            lst.append(i) #if word not in list, append to list
lst.sort() #sort list
print lst



#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief