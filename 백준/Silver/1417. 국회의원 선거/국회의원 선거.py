n = int(input())
vote = []

for _ in range(n) :
    x= int(input())
    vote.append(x)

cnt = 0
iam = vote.pop(0)

if n != 1 :
    while iam <= max(vote) :
        maxIndex = vote.index(max(vote))
        vote[maxIndex] -= 1
        iam += 1
        cnt += 1

print(cnt)