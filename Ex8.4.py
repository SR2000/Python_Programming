fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    wds= (line.rstrip()).split()
    for x in wds:
        if x not in lst:
            lst.append(x)
lst.sort()
print(lst)
