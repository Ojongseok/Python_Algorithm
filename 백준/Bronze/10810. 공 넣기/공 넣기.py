
n,m = map(int, input().split())
result=[0] * (n+1)

for r in range(m) :
    i,j,k = map(int, input().split())
    for v in range(i,j+1) :
        result[v] = k

for i in range(1,n+1) :
    print(str(result[i]) + " ", end='')