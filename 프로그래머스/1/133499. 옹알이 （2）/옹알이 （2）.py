def solution(babbling):
    answer = 0
    
    joka = ["aya", "ye", "woo", "ma"]
        
    for b in babbling:
        b = b.replace(joka[0], "1")
        b = b.replace(joka[1], "2")
        b = b.replace(joka[2], "3")
        b = b.replace(joka[3], "4")
        
        if any(x.isdigit()==False for x in b):
            continue
        else:
            isEnable = True
            
            for i, c in enumerate(b):
                if i >0 and b[i-1] == c:
                    isEnable=False
            if isEnable:
                answer+=1
        
    return answer