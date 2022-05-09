fname = input('Enter File:')
if len(fname) < 1 :
    fname = 'clown.txt'
hand = open(fname)


di = dict()
for line in hand:
    line = line.rstrip()
    #print(lin)
    wds = line.split()
    #print(wds)
    # going through all the words
    for w in wds:

        #print('**', w,di.get(w,-99))

        #if the key is not there, the count is zero
        #oldcount = di.get(w,0)
        #print(w, 'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
        #print(w, 'new', newcount)

        #if w in di:
        #    di[w] = di[w] + 1
        #    print('**Existing**')
        #else:
        #    di[w] = 1
        #    print('**New**')
        #print(di[w])

        #line 19-23 summery
        #idiom retieve/create/update counter
        di[w] = di.get(w, 0) + 1
        #print(w, 'new', di[w])

#print(di)

#find the most common words
largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k #cature/remember the word that was largest

print('Done', theword, largest)
