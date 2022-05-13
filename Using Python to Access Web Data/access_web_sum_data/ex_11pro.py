import re
print (sum( [ int(x) for x in re.findall('[0-9]+',open('833.txt').read()) ] ))

import re

name = input('Enter file: ')
if len(name) < 1:
    name = "242.txt"
handle = open(name)

sum = 0
lst = list()
for line in handle:
    line = line.rstrip()
    count = re.findall('[0-9]+', line)
    for x in range(len(count)):
        sum = int(count[x]) + sum

print('sum:', sum)
