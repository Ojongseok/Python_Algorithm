st = input()
numArr = [0] * 27

for i in range(ord('a'), ord('z')+1) :
    if chr(i) in st :
        numArr[i-97] = st.index(chr(i))
    else :
        numArr[i-97] = -1
for i in range(0, 26):
    print(numArr[i],end=" ")