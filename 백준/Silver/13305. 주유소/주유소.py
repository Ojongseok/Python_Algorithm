n = int(input())
placeDist = list(map(int, input().split()))
oil = list(map(int, input().split()))

nowFee = oil[0]
ans = nowFee * placeDist[0]

for i in range(1, n-1) :
    if (oil[i] > nowFee) :
        ans += nowFee * placeDist[i]
    else :
        nowFee = oil[i]
        ans += nowFee * placeDist[i]
print(ans)