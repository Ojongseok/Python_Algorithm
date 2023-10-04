n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n) :
    x,y = map(int, input().split())

    for i in range(x,x+10) :
        for j in range(y,y+10) :
            if (i < 101 and j < 101) :
                arr[i][j] = 1

ans = 0
for arr_in in arr :
    ans += arr_in.count(1)

print(ans)