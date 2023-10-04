n, count = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()

result = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n) :
            if count >= arr[i]+arr[j]+arr[k] > result:
                result = arr[i]+arr[j]+arr[k]
            else :
                continue

print(result)
