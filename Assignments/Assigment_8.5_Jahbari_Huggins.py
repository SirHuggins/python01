def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def printFrom(f,s):
    count = 0    
    for line in f:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
            if (len(line) >= 2):
                print line[1]
                count=count+1
    return count


fh = openFile()
sw = startsWith()
result = printFrom(fh,sw)
print "There were",result,"lines in the file with From as the first word"