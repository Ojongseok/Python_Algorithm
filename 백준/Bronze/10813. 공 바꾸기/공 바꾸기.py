n,m = map(int, input().split())
arr = [0] * (n+1)

for i in range(n+1) :
    arr[i] = i

for i in range(m) :
    a,b = map(int, input().split())
    arr[a],arr[b] = arr[b],arr[a]

for i in range(1,n+1):
    print(str(arr[i]) +" ", end='')