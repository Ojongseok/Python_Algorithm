def solution(dartResult):
    answer = 0
    
    result = [0,0,0,0]
    gop = {
        'S': 1,
        'D': 2,
        'T':3
    }
    
    dt=0
    for i, v in enumerate(dartResult) :
        if v.isdigit():
            if v == "1" and dartResult[i+1]=="0":
                dt+=1
                result[dt]=10
            else :
                if v=="0" and dartResult[i-1]=="1":
                    continue
                else :
                    dt+=1
                    result[dt]=int(v)
        elif v in gop.keys():
            result[dt]=result[dt]**gop[v]
        else :
            if v=="#":
                result[dt]=result[dt]*-1
            elif v=="*":
                result[dt]=result[dt]*2
                result[dt-1]=result[dt-1]*2
    answer=sum(result)    
    return answer