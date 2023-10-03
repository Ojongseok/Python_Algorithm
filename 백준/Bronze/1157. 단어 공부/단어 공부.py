a = input().upper()
num = [0]*100

for i in a : 
    num[ord(i)]+=1

max = max(num)

if num.count(max) == 1 :
    print(chr(num.index(max)))
else :
    print("?")