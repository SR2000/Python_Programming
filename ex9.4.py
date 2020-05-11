name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
wds = list()
emails = list()
counts = dict()
largestKey = None
largestVal = None
for line in handle :
    wds = (line.rstrip()).split()
    if len(wds) < 2:
        continue
    if wds[0] !='From':
        continue
    emails.append(wds[1])
for email in emails:
    counts[email]=counts.get(email,0) + 1
for k,v in counts.items():
    if largestKey is None or largestVal < v:
        largestKey = k
        largestVal = v
print(largestKey, largestVal)
