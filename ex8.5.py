fname = input("Enter file name: ")
fh = open(fname)
count = 0
wds = list()
for line in fh :
    wds = (line.rstrip()).split()
    if len(wds) < 2:
        continue
    if wds[0] !='From':
        continue
    print(wds[1])
    count=count + 1
print("There were", count, "lines in the file with From as the first word")
