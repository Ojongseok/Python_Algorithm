str = input()
answer = 0

croatia = ["c=", "c-","dz=","d-","lj","nj","s=","z="]

for i in croatia :
    str = str.replace(i, ".")

print(len(str))
