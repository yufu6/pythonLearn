fname = input('Enter File:')
if len(fname) < 1 :
    fname = 'clown.txt'
hand = open(fname)


di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1
#print(di)

#stored key value pair
#x = sorted(di.items())
#print(x[:5])

temp = list()
for k, v in di.items():
    #make new tuple, tuple is more efficient
    newt = (v, k)
    temp.append(newt)
#print('Flipped', temp)

#top 5 in high to low order value
temp = sorted(temp, reverse = True)
#print('Sorted ', temp[:5])

for v, k in temp[:5]:
    print(k, v)
