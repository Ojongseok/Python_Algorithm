n = int(input())

for i in range(n+1) :
    iToList = i + sum(list(map(int, str(i))))
    if (iToList == n) :
        print(i)
        exit() 
print(0)
