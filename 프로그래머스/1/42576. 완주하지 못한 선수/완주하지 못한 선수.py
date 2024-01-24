def solution(participant, completion):
    answer = ''
    
    p_dict = {}
    hash_sum=0
    
    for p in participant:
        p_dict[hash(p)] = p
        hash_sum+=hash(p)
    
    for c in completion:
        hash_sum-=hash(c)
    
    answer=p_dict[hash_sum]
    return answer