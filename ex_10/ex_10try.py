name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

name = list()
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    else:
        print(words)
        name.append(words)

print(name)
