n,l = map(int, input().split())
food = list(map(int, input().split()))

while any(l >= x for x in food) :
    a = min(food)
    l+=1
    food.remove(a)
print(l)