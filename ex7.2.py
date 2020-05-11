fname = input("Enter file name: ")
fh = open(fname)
val_tot=0
count=0
avg=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        pos=line.find('0.')
        val=float(line[pos:pos+6])
        val_tot=val_tot+val
        count=count+1
avg=val_tot/count
print('Average spam confidence:','%.12f'%avg)
