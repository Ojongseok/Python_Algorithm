def solution(numbers):
    answer = 0
    
    tens = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers :
        tens.remove(i)
        
    answer = sum(tens)
    
    return answer