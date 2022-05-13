score = input("Enter Score: ")
try:
    scoreInt = float(score)
    if scoreInt >= 0.9:
        print('A')
    elif scoreInt >= 0.8:
        print('B')
    elif scoreInt >= 0.7:
        print('C')
    elif scoreInt >= 0.6:
        print('D')
    else:
        print('F')

except:
    print('Error!')
