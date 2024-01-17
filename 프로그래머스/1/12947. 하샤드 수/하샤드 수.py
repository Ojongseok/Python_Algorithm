def solution(x):
    answer = False
    
    arrX = list(map(int, str(x)))
    
    if (x%sum(arrX)==0) :
        answer = True
    
    return answer