def solution(name, yearning, photo):
    answer = []
    
    yean_dict = {}
    
    for n,y in zip(name, yearning):
        yean_dict[n]=y
    
    for p in photo :
        hap = 0
        for i in p:
            if i in yean_dict.keys() :
                hap+=yean_dict[i]
        answer.append(hap)
    
    return answer