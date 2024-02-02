def solution(want, number, discount):
    answer = 0
    
    wants={}
    for w,n in zip(want,number):
        wants[w]=n
        
    for i in range(5):
        check= discount[i:i+10]
        w=wants.copy()
        for c in check:
            if c not in w.keys():
                break
            else :
                w[c]=w[c]-1
        if all(x==0 for x in list(w.values())):
            answer+=1
    
    return answer