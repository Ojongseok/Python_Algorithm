h, m = map(int, input().split())
time = int(input())

if m + time%60 >= 60 :
    h = h +1

m = (m + (time % 60)) % 60

h = (h + time//60) % 24

print(str(h) + " " + str(m))