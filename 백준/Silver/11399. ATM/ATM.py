n = int(input())
spend = list(map(int, input().split()))

spend.sort()
ans = 0
for i in range(n+1) : 
    for j in range(i) :
        ans +=spend[j]
print(ans)