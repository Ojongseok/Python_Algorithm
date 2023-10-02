n,m = map(int, input().split())

arr = [0] * (n+1)
for i in range(n+1):
    arr[i] = i

for i in range(m):
    x,y = map(int, input().split())
    for j in range(((y-x)//2)+1):
        arr[x+j],arr[y-j] = arr[y-j],arr[x+j]

for i in range(1,n+1):
    print(arr[i], end=" ")