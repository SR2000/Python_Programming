
import re
name = "regex_sum_242154.txt"
handle = open(name)
numbers = list()
count = 0
for line in handle :
    num = re.findall('[0-9]+',line)
    numbers = numbers + num
for n in numbers:
    count = count + int(n)
print('There are',len(numbers),'numbers in the file')
print('The sum of all numbers in the file is',count)
