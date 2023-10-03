n = int(input())
cnt = 0
for i in range(n) :
    st = list(input())
    arr = []
    for j in range(len(st)) :
        if not arr.__contains__(st[j]) :
            arr.append(st[j])
        else:
            if st[j] == st[j-1] :
                arr.append(st[j])
    if str(st) == str(arr) :
        cnt+=1
print(cnt)
