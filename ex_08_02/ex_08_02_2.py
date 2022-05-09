#prof way
fh = open('mbox-short.txt')

for line in fh:
    line = line.rstrip()

    #Gardian #1 Sart
    #if line == '':
        #print('Skip Blank')
        #continue
    #Gardian #1 End

    wds = line.split()
    #print('Words:', wds)

    #Gardian way 2 Sart make stronger gardian use <3
    #if len(wds) < 1:
        #continue
    #Gardian way 2 End

    #Gardian need come before or
    if len(wds) < 3 or wds[0] != 'From':
        #print('Ignore')
        continue
    print(wds[2])
