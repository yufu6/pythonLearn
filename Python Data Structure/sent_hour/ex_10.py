#10.2 Write a program to read through the mbox-short.txt and
#figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and
#then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lines = list()
count = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From '):
        continue
    else:
        #lines.append(words[5])
        lines.append(words[5].split(':')[0])

for time in lines:
    count[time] = count.get(time, 0) + 1

#print(sorted(count.items()))
for key, val in sorted(count.items()):
    print(key, val)

#for line in handle:
#    line = line.rstrip()
#    if line.startswith('From'):
#        continue
#    words = line.split()
#    print(words[2])
