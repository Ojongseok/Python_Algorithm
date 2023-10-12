s = list(map(int,input()))

zeroToOne = 0
zeroOn = False

oneToZero = 0
oneOn = False

for val in s :
    if zeroOn == False and val == 0 :
        zeroOn = True
        zeroToOne += 1
    elif val == 1:
        zeroOn = False


    if oneOn == False and val == 1 :
        oneOn = True
        oneToZero += 1
    elif val == 0 :
        oneOn = False

print(min(zeroToOne, oneToZero))
