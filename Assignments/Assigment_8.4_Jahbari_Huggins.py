def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def listWords(fh):
    lst = []
    for line in fh:
        line = ((line.rstrip()).lstrip()).split()
        for word in line:
            if word not in lst:
                lst.append(word)
    lst.sort()
    return lst


fh = openfile()
result = listWords(fh)
print result