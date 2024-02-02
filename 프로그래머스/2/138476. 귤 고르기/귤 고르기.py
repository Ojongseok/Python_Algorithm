def solution(k, tangerine):
    answer = 0
    
    t_dict={}
    
    for t in tangerine:
        if t in t_dict.keys():
            t_dict[t]+=1
        else :
            t_dict[t]=1
    t_list=list(t_dict.values())
    t_list.sort(reverse=True)
    
    for i in t_list:
        k-=i
        answer+=1
        if k<=0:
            break
    
    return answer