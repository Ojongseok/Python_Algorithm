m, n = map(int, input().split())
arr = [list(input()) for _ in range(m)]

ans_min = 64

for i in range(m - 7) :
    for j in range(n - 7) :
        min_start_b = 0
        min_start_w = 0

        for a in range(i, i+8) :
            for b in range(j, j+8) :
                if ((a+b)%2 == 0) :
                    if (arr[a][b] == 'B') :
                        min_start_w+=1
                    if (arr[a][b] == 'W') :
                        min_start_b+=1
                else :
                    if (arr[a][b] == 'B') :
                        min_start_b+=1
                    if (arr[a][b] == 'W') :
                        min_start_w+=1
        
        ans_min = min(ans_min, min_start_b, min_start_w)

print(ans_min)