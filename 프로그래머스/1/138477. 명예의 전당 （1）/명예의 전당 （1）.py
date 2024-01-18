def solution(k, score):
    answer = []
    
    golden = []
    for i in score :
        if len(golden)<k:
            golden.append(i)
        else :
            if min(golden) < i:
                golden.remove(min(golden))
                golden.append(i)
        
        answer.append(min(golden))
    
    return answer