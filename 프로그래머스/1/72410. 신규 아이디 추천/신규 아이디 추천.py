def solution(new_id):
    answer = ''
    
    st = ["-","_","."]
    
    id=new_id
    id=id.lower() # 1단계
    
    s=""
    for i in id:
        if i.isdigit() or i.islower() or i in st:
            s+=i
    id=s
    # 3단계
    while ".." in id:
        id=id.replace("..",".")
    #4
    if id and id[0]==".":
        id=id[1:]
    if id and id[-1]==".":
        id=id[:-1]
    #5
    if not id:
        id="a"
    #6
    if len(id)>=16:
        id=id[:15]
        if id[-1]==".":
            id=id[:-1]
            
    #7
    while len(id)<3:
        id+=id[-1]
    
    answer=id
    
    return answer