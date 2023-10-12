mathStr = input()

splitMinusList = mathStr.split('-')

for i, val in enumerate(splitMinusList) :
    if '+' in val :
        arr = list(map(int, val.split('+')))
        splitMinusList[i] = str(sum(arr))
    
ans = int(splitMinusList[0])

for i in range(1, len(splitMinusList)) :
    ans -= int(splitMinusList[i])

print(ans)