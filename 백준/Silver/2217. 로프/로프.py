n = int(input())
lopes = [int(input()) for _ in range(n)]
maxW = 0
lopes.sort()

for i, val in enumerate(lopes): 
    nowMax = val * (n-i)
    if val >= nowMax/(n-i):
        maxW = max(nowMax, maxW)

print(maxW)
