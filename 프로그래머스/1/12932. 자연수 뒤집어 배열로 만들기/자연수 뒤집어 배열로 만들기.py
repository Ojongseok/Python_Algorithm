def solution(n):
    answer = []
    
    reverseN = list(map(int, str(n)[::-1]))
    answer = reverseN
    
    return answer