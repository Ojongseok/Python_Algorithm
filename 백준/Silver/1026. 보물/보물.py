n = int(input())
A= list(map(int, input().split()))
B= list(map(int, input().split()))

minAns = 0

for _ in range(n) :
    minAns += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(minAns)