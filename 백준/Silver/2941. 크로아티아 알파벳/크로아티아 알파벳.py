str = input()
answer = 0

if "dz=" in str :
    answer += str.count("dz=")
    str = str.replace("dz=", ".")
if "c-" in str :
    answer += str.count("c-")
    str = str.replace("c-", ".")
if "c=" in str :
    answer += str.count("c=")
    str = str.replace("c=", ".")
if "d-" in str :
    answer += str.count("d-")
    str = str.replace("d-", ".")
if "lj" in str :
    answer += str.count("lj")
    str = str.replace("lj", ".")
if "nj" in str :
    answer += str.count("nj")
    str = str.replace("nj", ".")
if "s=" in str :
    answer += str.count("s=")
    str = str.replace("s=", ".")
if "z=" in str :
    answer += str.count("z=")
    str = str.replace("z=", ".")

str = str.replace(".","")
print(answer + len(str))