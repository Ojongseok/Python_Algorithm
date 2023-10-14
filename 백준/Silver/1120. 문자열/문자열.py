a,b = map(str, input().split())

minDiff = len(b)

for i in range(len(b) - len(a)+1) :
    checkStr = b[i:i+len(a)]
    diff = 0
    for j in range(len(a)) :
        if a[j] != checkStr[j] :
            diff += 1
    minDiff = min(diff, minDiff)
print(minDiff)