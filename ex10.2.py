name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
wds = list()
times = list()
hours = list()
counts = dict()
for line in handle :
    wds = (line.rstrip()).split()
    if len(wds) < 2:
        continue
    if wds[0] !='From':
        continue
    times.append(wds[5])
for time in times:
    hours.append(time[:2])
for hour in hours:
    counts[hour]=counts.get(hour,0) + 1
st = sorted(counts.items())
for k,v in st:
    print(k,v)
