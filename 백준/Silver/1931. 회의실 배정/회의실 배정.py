n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans=1

sortedTimeArr = sorted(arr, key=lambda x : (x[1], x[0]))

start = 0 
end = sortedTimeArr[0][1]

for i in range(1,n) :
    start = sortedTimeArr[i][0]
    if (start >= end) :
        end = sortedTimeArr[i][1]
        ans +=1
print(ans)