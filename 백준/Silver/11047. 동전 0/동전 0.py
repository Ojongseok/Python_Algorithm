n,k = map(int, input().split())
money = [int(input()) for _ in range(n)]
ans = 0
money.reverse()

for i in money :
    if (k >= i) :
        ans += k//i
        k = k%i

print(ans)
