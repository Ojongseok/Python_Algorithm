arr = [input() for _ in range(5)]

for j in range(15) :
    for i in range(5) :
        if (len(arr[i]) > j) :
            print(arr[i][j], end="")