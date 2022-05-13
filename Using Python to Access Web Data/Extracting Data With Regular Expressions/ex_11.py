import re

name = input('Enter file: ')
#if len(name) < 1:
#    name = "242.txt"
handle = open(name)

sum = 0
lst = list()
for line in handle:
    line = line.rstrip()
    count = re.findall('[0-9]+', line)
    #print(line, count)
    for i in range(len(count)):
        lst.append(count[i-1])

for j in range(len(lst)):
    sum = sum + int(lst[j])
print('sum:', sum)
